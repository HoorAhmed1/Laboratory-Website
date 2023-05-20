from django.shortcuts import render
from django.http import HttpResponse
from viewdata.models import Laboratory
# Create your views here.

def addlab(request):
    if request.method == "GET":
        return render(request , 'add_lab/Add_Lab.html')
    name = request.POST.get('textnames')
    id = request.POST.get('labId')
    buildingNumber = request.POST.get('buildingnumber')
    floorNum = request.POST.get('floornumber')
    pcNum = request.POST.get('pcnumber')
    chairNum = request.POST.get('chairnumber')
    capacity = request.POST.get('capacity')
    status = request.POST.get('s')

    data = Laboratory(labName=name, labID=id, buildingNum=buildingNumber, floorNum=floorNum, numOfPC=pcNum,numberOfChair=chairNum, labCapacity=capacity, Status=status)
    
    data.save()

    return render(request , 'add_lab/Add_Lab.html')