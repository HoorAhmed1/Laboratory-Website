from django.shortcuts import render
from django.http import HttpResponse
from viewdata.models import Device
# Create your views here.
def addpc(request):
    if request.method == "GET":
        return render(request , 'add_pc/Add_PC.html')
    PcID = request.POST.get('pc_id')
    labID = request.POST.get('lab_ID')
    new = request.POST.get('status1')
    repaired = request.POST.get('status2')

    data = Device(pcID= PcID, pc_labID=labID, new=new, repaired=repaired)
    
    data.save()
    return render(request , 'add_pc/Add_PC.html')