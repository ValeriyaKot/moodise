from . import views
from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()
router.register('pictures', views.PictureViewSet, basename='pictures')
router.register('boards', views.BoardViewSet, basename='boards')


urlpatterns = router.urls + [
    path('pictures/<int:pic_id>/board/<int:board_id>/', views.ManagePicInBoardView.as_view(), name='manage-pic-in-board')
]
