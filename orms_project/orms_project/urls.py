from xml.etree.ElementInclude import include
from django.urls import path

urlpatterns = [
    path('',include('user_app.urls')),
]
