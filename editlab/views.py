from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def editlab(request):
    return render(request , 'edit_lab/Edit_Lab.html')
