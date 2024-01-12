from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile, Follow, FollowInfo
from ..content.serializer import BoardSerializer
import json

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, use_url=True)

    class Meta:
        model = Profile
        fields = ('id', 'birthday', 'image', 'status')


class UserBaseInfoSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile', 'boards')


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile', 'auth_token')

    def get_auth_token(self, obj):
        refresh = RefreshToken.for_user(user=obj)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = "__all__"


class FollowersSerializer(serializers.ModelSerializer):
    follower = UserBaseInfoSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ("follower",)


class FollowingsSerializer(serializers.Serializer):
    following = UserBaseInfoSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ("following",)


class FollowInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = FollowInfo
        fields = ("followers_quantity", "followings_quantity")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    followers = FollowersSerializer(many=True, read_only=True)
    followings = FollowingsSerializer(many=True, read_only=True)
    follow_info = FollowInfoSerializer(read_only=True)
    boards = BoardSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile', 'followers', 'followings',
                  'follow_info', 'boards')

