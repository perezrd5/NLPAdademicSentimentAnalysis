from django.urls import path
from .views import DashoardView, RemoveSentiment


urlpatterns = [
    path('', DashoardView.as_view(), name='home'),
    path('delete-sentiments/<int:pk>', RemoveSentiment.as_view(), name='delete-sentiments')
]
