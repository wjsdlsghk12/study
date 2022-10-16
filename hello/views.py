from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def text(request,string):
    return render(request,'text.html',{'string':string})