from django.shortcuts import render
from .models import StatusInfo

# Create your views here.

def home(request):
    return render(request,"base.html")

def search(request):
    query = request.GET['search']
    data = StatusInfo.objects.filter(name__icontains=query)
    context = {"data":data}
    return render(request, "first.html", context)

def whole(request):
    alldata = StatusInfo.objects.order_by('-timestamp')
    context = {"alldata":alldata}
    return render(request, "second.html", context)

def next(request,id):
    data = StatusInfo.objects.get(sno=id)
    context = {"data":data}
    return render(request, "third.html", context)