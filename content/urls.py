from django.urls import path
from .views import ContentView

urlpatterns = [
    path('contents', ContentView.as_view()),
]