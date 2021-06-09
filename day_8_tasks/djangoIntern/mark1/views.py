from django.shortcuts import render
from django.http import HttpResponse, response
import os

def homepageview(request):
    return render(request,'home.html')


def aboutusview(request):
    return render(request,'about.html')    


def contactview(request):
    return render(request,'contact.html')    