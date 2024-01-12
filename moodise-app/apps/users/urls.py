from django.urls import path
from rest_framework import routers
from . import views
from django.contrib.auth.views import LogoutView


router = routers.SimpleRouter()
router.register('auth', views.AuthViewSet, basename='auth')
router.register('profiles', views.ProfileViewSet, basename='profile')
router.register('users', views.UserViewSet, basename='users')


urlpatterns = router.urls + [
    path('logout/', LogoutView.as_view()),
    path('profile/<int:pk>/follow/', views.FollowUser.as_view(), name='follow-user')
]

