from django.contrib.auth import logout
from django.core.exceptions import ImproperlyConfigured
# from django.http import Http404
from rest_framework import viewsets, status, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
# from rest_framework.generics import get_object_or_404
from . import serializer
from .utils import get_and_authenticate_user, create_user_account
from .models import Profile, FollowInfo, Follow


User = get_user_model()


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializer.ProfileSerializer

    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    # permission_classes = [IsAuthenticated]


class AuthViewSet(viewsets.GenericViewSet):
    queryset = ''
    permission_classes = [AllowAny, ]
    serializer_classes = {
        'login': serializer.UserLoginSerializer,
        'register': serializer.UserRegisterSerializer,
        'password_change': serializer.PasswordChangeSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializers.validated_data)
        data = serializer.AuthUserSerializer(user, context={"request": request}).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = create_user_account(**serializers.validated_data)
        user.save()
        Profile.objects.create(user=user)
        FollowInfo.objects.create(user=user)
        data = serializer.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Successfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()


class FollowUser(views.APIView):


    def post(self, request, pk):
        target_user = User.objects.get(profile__id=pk)
        request_user = User.objects.get(id=request.user.id)
        user_follow_info, obj = FollowInfo.objects.get_or_create(user=target_user)
        request_user_follow_info, obj = FollowInfo.objects.get_or_create(user=request_user)
        serializers = serializer.FollowSerializer(data={"follower": request_user.id, "following": target_user.id})
        if target_user != request_user:
            if serializers.is_valid():
                serializers.save()
                user_follow_info.followers_quantity = len(target_user.followings.all())
                request_user_follow_info.followings_quantity = len(request_user.followers.all())
                user_follow_info.save()
                request_user_follow_info.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
        elif target_user == request_user:
            return Response("You can not follow yourself", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        target_user = User.objects.get(profile__id=pk)
        request_user = User.objects.get(id=request.user.id)
        user_follow_info, obj = FollowInfo.objects.get_or_create(user=target_user)
        request_user_follow_info, obj = FollowInfo.objects.get_or_create(user=request_user)
        follow = Follow.objects.get(follower=request_user.id, following=target_user.id)
        if target_user != request_user:
            follow.delete()
            user_follow_info.followers_quantity = len(target_user.followings.all())
            request_user_follow_info.followings_quantity = len(request_user.followers.all())
            user_follow_info.save()
            request_user_follow_info.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif target_user == request_user:
            return Response("You can not unfollow yourself", status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


