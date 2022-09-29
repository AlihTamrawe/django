from django.urls import path 
from . import views

urlpatterns = [
    path('',views.root),
    path('shows/', views.toshownew),
    path('shows/new/', views.insert),
    # path('create/',views.insert),
    path('shows/<int:id>', views.details),
    path('shows/<int:id>/edit', views.edit),
    path('delete/<int:id>',views.deleteme),


]