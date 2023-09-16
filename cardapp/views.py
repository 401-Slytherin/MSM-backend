from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import CardModel
from .permissions import IsOwnerOrReadOnly
from .serializers import CardSerializer


def card_image(request, card_id):
    card = CardModel.objects.get(pk=card_id)
    if card is not None:
        return render(request, "cards/card.html", {'card': card})
    else:
        raise Http404('Card does not exist')


class CardList(ListCreateAPIView):

    # incase we need to display all cards (can possibly use in another view)
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):

        card_name = request.data["card_name"]
        owner = request.data["owner"]
        image = request.data["image"]
        condition = request.data["condition"]
        category = request.data["category"]
        description = request.data["description"]
        price = request.data["price"]
        year_set = request.data["year_set"]
        card_num = request.data["card_num"]
        promotional = request.data["promotional"]

        CardModel.objects.create(
            card_name=card_name,
            owner=owner,
            image=image,
            condition=condition,
            category=category,
            description=description,
            price=price,
            year_set=year_set,
            card_num=card_num,
            promotional=promotional
        )

        return Response("Card created successfully!", status=status.HTTP_201_CREATED)

    # def get_queryset(self):
    #     user = self.request.user
    #     return CardModel.objects.filter(owner=user)

class CardListDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer
