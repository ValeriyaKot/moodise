from django.shortcuts import get_object_or_404
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from .serializer import PictureSerializer, BoardSerializer
from .models import Picture, Board
from django.contrib.auth.models import User


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ManagePicInBoardView(views.APIView):

    def post(self, request, board_id, pic_id):
        board = get_object_or_404(Board, id=board_id)
        picture = get_object_or_404(Picture, id=pic_id)
        board.images.add(picture)
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request, board_id, pic_id):
        board = get_object_or_404(Board, id=board_id)
        picture = get_object_or_404(Picture, id=pic_id)
        board.images.remove(picture)
        return Response(status=status.HTTP_201_CREATED)
