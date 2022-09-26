from django.urls import path
from . import views

urlpatterns = [
        path('',views.root2),
        path('blog', views.index2),

]