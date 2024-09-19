from django.contrib import admin

from . models import Todo
# Register your models here.

class Todoadmin(admin.ModelAdmin):
    list_display=['is_completed','text','updated_at','created_at']
    
admin.site.register(Todo,Todoadmin)