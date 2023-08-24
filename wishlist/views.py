from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import FavouriteItem
from .serializers import FavouriteItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

class FavouriteListView(generics.ListAPIView):
    serializer_class = FavouriteItemSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FavouriteItem.objects.filter(user=self.request.user)

class AddToFavouritesView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, item_type, item_id):
        content_type = get_object_or_404(ContentType, model=item_type)
        FavouriteItem.objects.get_or_create(user=request.user, content_type=content_type, object_id=item_id)
        return Response({'message': 'Added to favourites successfully.'})

class RemoveFromFavouritesView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        FavouriteItem.objects.filter(user=request.user, id=item_id).delete()
        return Response({'message': 'Removed from favourites successfully.'})