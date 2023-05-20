from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def displayhome(request):
    return render(request , 'home/Home.html')
    # return HttpResponse('hello world')
 