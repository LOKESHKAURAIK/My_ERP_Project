from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student,Course,Amount
def index(request):
    cr=Course.objects.all()
    return render(request,"index.html",{"cr":cr})

def addcourse(request):
    if request.method=="POST":
        c=Course()
        c.cname=request.POST['cname']
        c.duration=request.POST['duration']
        c.detail=request.POST['details']
        f=request.POST['fees']
        c.fees=int(f)
        c.save()
        messages.info(request,"courses add sucessfully")
        return redirect('/')
    else:
        return render(request,"addcourse.html")

def showcourse(request):
    cr=Course.objects.all()
    return render(request,"showcourse.html",{"cr":cr})