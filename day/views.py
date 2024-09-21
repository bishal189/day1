from django.shortcuts import render,HttpResponse,redirect
from . models import Todo
# Create your views here.

def home(request):
    if request.method == 'POST':
        data=request.POST['kushalta']
        Todo.objects.create(
            is_completed=True,
            text=data
            
        )
        return redirect('home')
        
    else:
        data=Todo.objects.all()
        context={
            'datas':data
        }
        return render(request,'index.html',context)
    
