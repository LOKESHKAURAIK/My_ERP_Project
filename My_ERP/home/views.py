from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Student,Course,Amount
import datetime

def index(request):
    if request.method=='POST':
        s=Student()
        s.sname=request.POST['sname']
        s.email=request.POST['email']
        s.mobile=request.POST['mob']
        s.branch=request.POST['branch']
        cr=request.POST.getlist('course')    # hame multiple course add karne hai , so use getlist()
        for i in cr:
            s.course=Course.objects.get(id=i)
        s.status=request.POST['status']
        s.date=datetime.datetime.now()
        s.address=request.POST['address']
        s.qualification=request.POST['qualification']
        s.sem=request.POST['sem']
        p=request.POST['passout']
        s.passout=int(p)
        s.save()
        messages.info(request,'student added successfully..!')
        return redirect('/')
    else:
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

def showstudent(request):
    stu=Student.objects.all()
    return render(request,"showstudent.html",{"stu":stu})