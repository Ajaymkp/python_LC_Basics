from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class Emp_add(View):
    def get(self,request):
        data={
            "emp_form" : Emp_form()
        } 
        return render(request,"emp_add.html",data)
    def post(self,request):
        abc=Emp_form(request.POST)
        if abc.is_valid():
            abc.save()
        return redirect("/cbv/empview/")
class Emp_view(View):
    def get(self,request):
        data={
            "alldata":Employee.objects.all()
        }
        return render(request,"emp_view.html",data)

class Emp_update(View):
    def get(self,request,id):
        selected=Employee.objects.get(id=id)
        data={
            "emp_form":Emp_form(instance=selected)
        }    
        return render(request,"emp_add.html",data)
    def post(self,request,id):
        selected=Employee.objects.get(id=id)
        abc=Emp_form(request.POST,instance=selected)
        if abc.is_valid():
            abc.save()
        return redirect("/cbv/empview/")   
class Emp_Delete(View):
    def get(self,request,id):
        selected=Employee.objects.get(id=id)
        selected.delete()
        return redirect("/cbv/empview")     
        
