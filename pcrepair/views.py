from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from viewdata.models import BrokenPC


def ajax(request):
    broken = list(BrokenPC.objects.values())
    return JsonResponse(broken, safe=False)

def index(request):
    ajax(request)
    return render(request, 'pc_repair/PC_Repair.html' )

def pcrepair(request):
    # context = BrokenPC.objects.all()   
    return render(request , 'pc_repair/PC_Repair.html',{'broken':BrokenPC.objects.all()})




# def index(request):
#     ajax(request)
#     return render(request, 'search/search.html' )

# def search(request):
#     return render(request , 'search/search.html', {'lab':Laboratory.objects.all()})