from django.urls import path 
from . import views

urlpatterns = [
    path('',views.root),
    path('success/', views.index),
    path('logout/',views.out),
    
]