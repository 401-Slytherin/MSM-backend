from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
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

    # def get_queryset(self):
    #     user = self.request.user
    #     return CardModel.objects.filter(owner=user)

class CardListDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer
