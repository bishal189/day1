from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    
    path('completed/<int:id>/',views.completed,name='com'),
    
    path('uncompleted/<int:id>/',views.uncompleted,name='uncom'),
   
]

