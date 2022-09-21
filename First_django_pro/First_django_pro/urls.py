from django.urls import path,include


urlpatterns = [
    path('',include('registration.urls')),
    path('first_app/',include('first_app.urls')),
]
