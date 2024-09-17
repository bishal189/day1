from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    
    path('bishal/',views.bishal,name='bishal'),
    
    path('dinesh/',views.dinesh,name='dinesh')
   
]
