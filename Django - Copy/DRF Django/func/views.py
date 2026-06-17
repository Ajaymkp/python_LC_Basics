from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# Create your views here.

@api_view(["POST"])
def add_data(request):
    abc=Stud_serializer(data=request.data)
    if abc.is_valid():
        abc.save()
    return Response("data added")

# @api_view(["GET"])
# def view_data(request):
#     abc=Student.objects.all()
#     result = []
#     for i in abc:
#         a={
#             "id" : i.id,
#             "name" : i.name,
#             "batch" : i.batch
#         }
#         result.append(a)
#     return Response(result)


@api_view(["Get"])
def view_data(request):
    all_data = Student.objects.all()
    result=Stud_serializer(all_data,many=True).data
    return Response(result)
@api_view(["Get"])
def view_id(request,id):
    selected=Student.objects.get(id=id)
    result=Stud_serializer(selected).data
    return Response(result)

@api_view(["patch"])
def patch_data(request,id):
    selected=Student.objects.get(id=id)
    result=Stud_serializer(selected,data=request.data)
    if result.is_valid():
        result.save()
    return Response("data added successfully")

@api_view(["delete"])
def delete_data(request,id):
    selected=Student.objects.get(id=id)
    selected.delete()
    return Response ("data deleted successfully")





