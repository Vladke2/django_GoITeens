from django.urls import path
from user_drf.views import (UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    FilteredUserListAPIView,
    AdultUserListAPIView
)


urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('filtered/', FilteredUserListAPIView.as_view()),
    path('adult_users/', AdultUserListAPIView.as_view()),
    ]
