from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(' hi i am bishal ')
    
    
def bishal(request):
    return HttpResponse('hello world')    


def dinesh(request):
    return  HttpResponse(' i am dinesh')