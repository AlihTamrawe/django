from django.urls import path 
from . import views

urlpatterns = [
    path('counter/', views.index),
    path('reset/',views.destroy),
]