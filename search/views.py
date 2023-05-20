from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from viewdata.models import Laboratory
# from django.http import JsonResponse
# Create your views here.



# def search2(request):
#     return render(request , 'search/labs.html', {'lab':Lab.objects.all()})

def ajax(request):
    lab = list(Laboratory.objects.values())
    return JsonResponse(lab, safe=False)


def index(request):
    ajax(request)
    return render(request, 'search/search.html' )

def search(request):
    return render(request , 'search/search.html', {'lab':Laboratory.objects.all()})