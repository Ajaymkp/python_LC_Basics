from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.

class Emp_view(APIView):
    def post(self,request):
        print(request.data)
        abc = Employee(name=request.data["name"],
                       dept=request.data["dept"],
                       salary=request.data["salary"])
        abc.save()
        return Response ("data post successfully")
      
    def get(self,request):
        abc = Employee.objects.all()
        data =[]
        for i in abc:
            a={
               "name":i.name,
               "dept":i.dept,
               "salary":i.salary 
            }
            data.append(a)
        return Response(data)

    # def get(self,request):
    #     abc = Employee.objects.all()
    #     data = {
    #            "name":abc.name,
    #            "dept":abc.dept,
    #            "salary":abc.salary 
    #     }
    #     return Response(data)
    
    
class Emp_id(APIView):
    def get(self,request,id):
        abc = Employee.objects.get(id=id)
        data = {
            "name":abc.name,
            "dept":abc.dept,
            "salary":abc.salary
        }
        return Response (data)
    def put(self,request,id):
        abc = Employee.objects.filter(id=id)
        abc.update(name=request.data["name"],
                   dept=request.data["dept"],
                   salary=request.data["salary"]
        )
        return Response("data updated successfully")
    def patch(self,request,id):
        abc = Employee.objects.filter(id=id)
        abc.update(name=request.data["name"],
                   dept=request.data["dept"],
                   salary=request.data["salary"]
        )
        return Response("data updated successfully")
    def delete(self,request,id):
        abc = Employee.objects.get(id=id)
        abc.delete()
        return Response("that is it for the day")