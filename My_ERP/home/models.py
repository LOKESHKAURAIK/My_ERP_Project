from django.db import models

class Course(models.Model):
    cname = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    fees = models.IntegerField()
    def __str__(self):
        return self.cname+" "+str(self.fees)
    

class Student(models.Model):
    sname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateField(auto_now=False)
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    sem = models.CharField(max_length=50)
    passout = models.IntegerField()

    def __str__(self):
        return self.sname+" "+str(self.course)
    

class Amount(models.Model):
    student = models.OneToOneField(Student, primary_key=True,on_delete=models.CASCADE)
    total_fees = models.IntegerField()
    remaining = models.IntegerField()
    submitamount = models.CharField(max_length=50)
    submitdate = models.CharField(max_length=50)
    nextpaydate = models.DateField(auto_now=False)

    def __str__(self):
        return self.student.sname+" "+str(self.remaining)
    


