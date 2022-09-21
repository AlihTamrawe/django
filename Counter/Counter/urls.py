from django.urls import path,include


urlpatterns = [
    path('',include('count_app.urls'))
]
