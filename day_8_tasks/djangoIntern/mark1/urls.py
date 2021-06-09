from django.urls import path
from . import views
import os

urlpatterns =[
    path('',views.homepageview,name="home"),
    path('about',views.aboutusview,name="aboutus"),
    path('contact',views.contactview,name="contactus"),
]