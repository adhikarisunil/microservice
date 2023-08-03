from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView
from users.views import UserListCreateView, UserRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'users', UserListCreateView)
router.register(r'users', UserRetrieveUpdateDestroyView)

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]
