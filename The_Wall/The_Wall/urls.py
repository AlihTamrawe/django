from django.urls import path,include

urlpatterns = [
    path('wall/',include('wall_app.urls')),
    path('',include('login_app.urls')),

]
