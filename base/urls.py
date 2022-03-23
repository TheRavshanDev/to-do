from django.urls import path
from .views import DeleteView, HomeView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('<pk>/',DeleteView.as_view(), name='delete'),
]