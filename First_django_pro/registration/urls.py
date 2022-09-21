from django.urls import path
from . import views


urlpatterns = [
        path('', views.welcome),  
        path('student/<str:student>/<int:id2>', views.one_method),  
        path('users',views.users_show),
        
        # path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
        # path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    	# path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
]