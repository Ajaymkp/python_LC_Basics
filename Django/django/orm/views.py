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

