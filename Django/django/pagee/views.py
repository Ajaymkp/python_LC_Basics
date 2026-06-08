from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

def paper(request):
    alldata = Note.objects.all()
    abc = Paginator(alldata, 3)
    page_number = request.GET.get('page')
    data = abc.get_page(page_number)
    return render(request, 'page.html', {
        'page_obj' : data
    })