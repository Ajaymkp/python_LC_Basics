from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

class Emp(APIView):
    def post(self,request):
        print(request.data)
        emp = Employee(name=request.data["name"],
                       dept=request.data["dept"],
                       salary=request.data["salary"])
        emp.save()
        return Response("data added success fully")
    
    def get(self,request):
        emp = Employee.objects.all()
        data = []
        for i in emp:
            a = {
                "name":i.name,
                "dept":i.dept,
                "salary":i.salary
            }
            data.append(a)
        return Response(data)
    
class Emp_id (APIView):    
    def get (self,request,id):
        abc = Employee.objects.get(id=id)
        result = {
            "name":abc.name,
            "dept":abc.dept,
            "salary":abc.salary
        }
        return Response(result)
    def put(self,request,id):
        abc = Employee.objects.filter(id=id)
        print(request.data)
        abc.update(name=request.data["name"],
                   dept=request.data["dept"],
                   salary=request.data["salary"])
        return Response("data updated successfully")
    def patch(self,request,id):
        abc = Employee.objects.filter(id=id)
        print(request.data)
        abc.update(name=request.data["name"],
                   dept=request.data["dept"],
                   salary=request.data["salary"])
        return Response("data updated successfully")
    
    def delete(self,request,id):
        abc = Employee.objects.filter(id=id)
        abc.delete()
        return Response("data deleted successfully")