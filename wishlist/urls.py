from django.urls import path
from .views import FavouriteListView, AddToFavouritesView, RemoveFromFavouritesView

urlpatterns = [
    path('api/favourites/', FavouriteListView.as_view(), name='favourites'),
    path('api/add_to_favourites/<str:item_type>/<int:item_id>/', AddToFavouritesView.as_view(), name='add_to_favourites'),
    path('api/remove_from_favourites/<int:item_id>/', RemoveFromFavouritesView.as_view(), name='remove_from_favourites'),
]