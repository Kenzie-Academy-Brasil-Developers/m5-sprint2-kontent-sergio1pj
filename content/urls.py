from django.urls import path
from .views import ContentView, ContentDetailView, ContentViewFilter

urlpatterns = [
    path('contents', ContentView.as_view()),
    path('contents/<int:pk>', ContentDetailView.as_view()),
    path('contents/filter/', ContentViewFilter.as_view()),
]