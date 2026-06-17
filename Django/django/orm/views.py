from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def create_data(request):
    author,_=Author.objects.get_or_create(name="beners",city="newyork")

    Book.objects.create(title="html",author=author,date="1999-05-23",price="200")
    return HttpResponse("data added sucess fully")


def view_data(request):
    books=Book.objects.all()
    result="<h1> book list </h1>"
    for b in books:
        result=result+f"<pre>{b.title}        {b.author}      {b.date}        {b.price}</pre>"
    return HttpResponse(result)    
# select * from book;

def filter_data(request):
    books=Book.objects.filter(price__gt=200)
    result="<h1> book list price in above 200</h1>"
    for b in books:
        result=result+f"<pre>{b.title}        {b.author}      {b.date}        {b.price}</pre>"
    return HttpResponse(result) 
    
# select * from book where price>200;

def order_by_asc(request):
    books=Book.objects.order_by("date")
    result="<h1> book list price in above 200</h1>"
    for b in books:
        result=result+f"<pre>{b.title}        {b.author}      {b.date}        {b.price}</pre>"
    return HttpResponse(result) 

# select * from book order_by date;

def order_by_slice(request):
    books=Book.objects.order_by("date")[:2]
    result="<h1> book list price in above 200</h1>"
    for b in books:
        result=result+f"<pre>{b.title}        {b.author}      {b.date}        {b.price}</pre>"
    return HttpResponse(result) 

# select * from book order_by date limit 2;


def order_by_desc(request):
    books=Book.objects.order_by("-price")
    result="<h1> book list price in above 200</h1>"
    for b in books:
        result=result+f"<pre>{b.title}        {b.author}      {b.date}        {b.price}</pre>"
    return HttpResponse(result) 

# select * from book order_by price desc;

def delete_data(request):
    book=Book.objects.get(id=1)
    book.delete()
    return HttpResponse("data deleted successfully")

# select * from book where id=1;


# select_related

# e=Emp.objects.all()
# for i in e:
#     print(i.name)
#     print(i.dept.name)

# SELECT * FROM emp;

# select * from dept where id=2;
# select * from dept where id=2;
# select * from dept where id=1;


def select_related(request):
    e=Emp.objects.select_related("dept").all()

    return render(request,"select_related.html",{"data":e})




# e=Emp.objects.select_related("dept").all()
# select Emp.name,Department.name from Emp inner join Department where Emp.id=Department.id;


def prefetch_related(request):
    s=Student.objects.prefetch_related("course")
      

    return render(request,"prefetch.html",{"data":s})




