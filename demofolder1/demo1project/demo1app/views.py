from django.http import HttpResponse
from django.shortcuts import render
from .models import places, team


# Create your views here.


def demo(request):
    obj=places.objects.all()
    obj1=team.objects.all()
    return   render(request,"index.html",{'result':obj,'result1':obj1})


#def calculate(request):
    #return   render(request,"calculate.html")


#def addition(request):
 #   a=int(request.GET['num1'])
  #  b=int(request.GET['num2'])
   # result1=a+b
    #result2=a-b
    #result3=a*b
    #result4=a/b
    #return render(request,'result.html',{'answer1':result1,'answer2':result2,'answer3':result3,'answer4':result4})


#def subtraction(request):
 #   a=int(request.GET[ 'num1'])
  #  b=int(request.GET['num2'])
   # result2=a-b
    #return render(request,'result.html',{'answer2':result2})

#def contact(request):
 # return HttpResponse('XYZ HOUSE,PQR,SAHGHSDH')


#def detail(request):
 # return render(request, "tmp2.html")


#def thanks(request):
  #return render(request, "tmp3.html")


#def about(request):
 # return render(request, "tmp4.html")