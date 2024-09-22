from django.shortcuts import render,HttpResponse,redirect
from . models import Todo
# Create your views here.

def home(request):
    if request.method == 'POST':
        data=request.POST['kushalta']
        Todo.objects.create(
            # is_completed=True,
            text=data
            
        )
        return redirect('home')
        
    else:
        data=Todo.objects.filter(is_completed=False)
        iscompleted=Todo.objects.filter(is_completed=True)
        context={
            'datas':data,
            'iscompleted':iscompleted
        }
        return render(request,'index.html',context)
    
    
 
def delete_item(request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('home')
    
    
    
def completed(request,id):
    data=Todo.objects.get(id=id)
    data.is_completed=True
    data.save()
    return redirect('home')    


def uncompleted(request,id):
    data=Todo.objects.get(id=id)
    data.is_completed=False
    data.save()
    return redirect('home')
    