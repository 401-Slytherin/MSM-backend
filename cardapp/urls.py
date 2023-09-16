from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import CardList, CardListDetail, card_image

urlpatterns = [
    path("", CardList.as_view(), name="card_list"),
    path("<int:pk>/", CardListDetail.as_view(), name="card_list_detail"),
    path("", card_image, name="card.html"),
    # TODO: create url for card image
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
