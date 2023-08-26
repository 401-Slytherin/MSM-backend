from django.urls import path
from .views import ProfileView, ProfileUpdateView, UserDeleteView

urlpatterns = [
    path('api/profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('api/profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('api/profile/delete/', UserDeleteView.as_view(), name='user-delete'),
]
