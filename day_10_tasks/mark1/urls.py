from django.urls import path
from . import views
import os

urlpatterns =[
    path('',views.homepageview,name="home"),
    path('about',views.aboutusview,name="aboutus"),
    path('contact',views.contactview,name="contactus"),
    path('myform',views.myform,name="myform"),
    path('formprocess',views.process,name='process'),
    path('slist',views.studentlist.as_view(),name='s1'),
]