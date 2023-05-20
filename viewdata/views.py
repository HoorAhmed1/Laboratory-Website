from django.shortcuts import render
from .models import Laboratory
# Create your views here.

def read(req):
    lab = Laboratory.objects.all()
    passing = {'labs' : lab}
    return render(req , 'search/Search.html', context={'labs' :lab})