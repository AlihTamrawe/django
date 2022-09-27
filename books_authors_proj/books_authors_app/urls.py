from django.urls import path 
from . import views

urlpatterns = [
    path('', views.insert),
    path('author/',views.add1),
    path('book/<int:num>',views.fun),
    path('author/<int:num>',views.shows)
]