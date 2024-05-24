from django.urls import path
from .views import PetsListCreateAPIView, PetRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('pets/',PetsListCreateAPIView.as_view()),
    path('pets/<int:pk>/', PetRetrieveUpdateDestroyAPIView.as_view())

]

