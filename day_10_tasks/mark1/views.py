from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.generic import ListView
from .models import Contact_us, Student

def homepageview(request):
    return render(request,'home.html')


def aboutusview(request):
    return render(request,'about.html')    


def contactview(request):
    return render(request,'contact.html')  

def myform(request):
    return render(request,'myform.html')     

def process(request):
    print("Welcome")  
    print(request.method)
    print(request.POST)
    fname = (request.POST['fname'])
    lname = (request.POST['lname'])
    mail = (request.POST['email'])
    dob = (request.POST['dob'])
    mobile = int(request.POST['mobile'])

    contact_us = Contact_us(fname = fname,lname= lname,mail=mail,dob = dob,mobile=mobile)
    contact_us.save()
    
    return render(request,'home.html')   

class studentlist(ListView):
    model = Student
    template_name = 'slist.html'
         
def ans(request):
    data = Contact_us.objects.all()
    print(data)
    context = {'contacts':data}
    return render(request,'ans.html',context)