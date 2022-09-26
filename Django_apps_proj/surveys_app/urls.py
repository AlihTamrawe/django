from django.urls import path
from . import views

urlpatterns = [
        path('',views.root3),
        path('jamal', views.index3),

]