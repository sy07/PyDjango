from django.shortcuts import render
from django.http import HttpResponse, response
import os

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
    mobile = (request.POST['mobile'])
    
    return render(request,'ans.html',{'fname':fname,'lname':lname,'mail':mail,'dob':dob,'mobile':mobile})    