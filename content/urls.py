from django.urls import path
from .views import ContentView, ContentDetailView

urlpatterns = [
    path('contents', ContentView.as_view()),
    path('contents/<int:pk>', ContentDetailView.as_view()),
]