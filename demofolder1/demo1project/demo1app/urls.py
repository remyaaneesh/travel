from django.contrib import admin
from django.urls import path,include
from . import  views


urlpatterns = [
    path('',views.demo,name="demo"),
    #path('add/',views.addition,name='addition'),
   #path('about/',views.about,name="about"),
#path('contact/',views.contact,name="contact"),
#path('detail/',views.detail,name="details"),
#path('thanks/',views.thanks,name="thanks")

]