from django.urls import path
from post.views import deneme, netice

urlpatterns = [
    path('',deneme),
    path('netice/', netice)
]