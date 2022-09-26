from django.urls import path,include

urlpatterns = [
    path('blogs/',include('blogs_app.urls')),
    path('surveys/',include('surveys_app.urls')),
    path('',include('user_app.urls')),

]
