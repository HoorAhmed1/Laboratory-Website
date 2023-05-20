from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'all_projects/All_Projects.html')