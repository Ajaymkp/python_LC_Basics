from django.shortcuts import render,HttpResponse,redirect
from .forms import *
from .models import *



def func(request):
    return HttpResponse("hi hello")

def html(request):
    data={
        "name":"django",
        "topic":"intro",
        "a":[1,2,3,4,5]
    }
    return render(request,"index.html",data)

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contact.html")

def student(request):
    data={
        "Studform":Stud_form()
    }

    if request.method=="POST":
        print(request.POST)
        abc=Stud_form(request.POST)
        if abc.is_valid():
            abc.save()
            return redirect("/myapp/view/")
    return render(request,"studadd.html",data)

def view(request):
    data={
        "alldata":Student.objects.all()
    }
    return render(request,"studview.html",data)

def student_update(request,id):
    selected_student=Student.objects.get(id=id)
    data={
        "Studform":Stud_form(instance=selected_student)
    }
    if request.method=="POST":
        xyz=Stud_form(request.POST,instance=selected_student)
        if xyz.is_valid():
            xyz.save()
            return redirect("/myapp/view/")
    return render(request,"studadd.html",data)

def student_delete(request,id):
    selected_student=Student.objects.get(id=id)
    selected_student.delete()
    return redirect("/myapp/view/")



