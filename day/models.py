from django.db import models

# Create your models here.

class Todo(models.Model):
    is_completed=models.BooleanField(default=False)
    text=models.CharField(max_length=100)
    
    
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.text 
