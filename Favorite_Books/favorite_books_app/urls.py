from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),    
    path('<int:id>/',views.like),
    path('like/<int:id2>/',views.do_like),
]