from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse("Welcome Mark#1 to HomePage")


def aboutusview(request):
    return HttpResponse("Welcome Mark#1 to About us")    


def contactview(request):
    return HttpResponse("Welcome Mark#1 to Contact Us")    