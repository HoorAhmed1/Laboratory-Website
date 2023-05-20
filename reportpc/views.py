from django.shortcuts import render
from django.http import HttpResponse
from viewdata.models import BrokenPC
# Create your views here.

def reportpc(request):
    if request.method == "GET":
        return render(request , 'report_pc/Report_PC.html')
    PcID = request.POST.get('pcID')
    labID = request.POST.get('labID')
    ProblemType = request.POST.get('os')
    date = request.POST.get('date')
    description = request.POST.get('Description')

    data = BrokenPC(BrokenID=PcID, LabId=labID, date=date, ProblemType=ProblemType, description=description)
    data.save()
    return render(request , 'report_pc/Report_PC.html')