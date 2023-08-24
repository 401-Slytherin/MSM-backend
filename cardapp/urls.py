from django.urls import path
from .views import CardList, CardListDetail

urlpatterns = [
    path("", CardList.as_view(), name="card_list"),
    path("<int:pk>/", CardListDetail.as_view(), name="card_list_detail"),
    # path("media/images/")
    # TODO: create url for card image
]