from django.shortcuts import render,redirect,HttpResponse
from .forms import *

def product_add(request):
    data={
        "productform":Product_form()
    }
    if request.method=="POST":
        print(request.POST)
        abc=Product_form(request.POST)
        if abc.is_valid():
            abc.save()
        else:
            print("data too long")  
        return redirect("/mysql/view/")     
    return render(request,"p_add.html",data)

def product_view(request):
    data={
        "all_data":Product.objects.all()
    }
    return render(request,"p_view.html",data)

def product_update(request,id):
    selective=Product.objects.get(id=id)
    data={
        "productform":Product_form(instance=selective)
    }
    if request.method=="POST":
        xyz=Product_form(request.POST,instance=selective)
        if xyz.is_valid():
            xyz.save()
        return redirect("/mysql/view/") 
    return render(request,"p_add.html",data)


def product_delete(request,id):
    selective=Product.objects.get(id=id)
    selective.delete()
    return redirect("/mysql/view/")



def cust_add(request):
    data={
        "customerform":Customer_form()
    }
    if request.method=="POST":
        print(request.POST)
        abc=Customer_form(request.POST)
        if abc.is_valid():
            abc.save()
        else:
            print("data too long")  
        return redirect("/mysql/custview/")     
    return render(request,"cust_add.html",data)

def cust_view(request):
    data={
        "all_data":Customer.objects.all()
    }
    return render(request,"cust_view.html",data)

def cust_update(request,id):
    selective=Customer.objects.get(id=id)
    data={
        "customerform":Customer_form(instance=selective)
    }
    if request.method=="POST":
        xyz=Customer_form(request.POST,instance=selective)
        if xyz.is_valid():
            xyz.save()
        return redirect("/mysql/custview/") 
    return render(request,"cust_add.html",data)


def cust_delete(request,id):
    selective=Customer.objects.get(id=id)
    selective.delete()
    return redirect("/mysql/custview/")

def order_add(request):
    data={
        "orderform":Order_form()
    }
    if request.method=="POST":
        product_amount=Product.objects.get(id=request.POST["product_refer"])
        quantity=request.POST["quantity"]
        total_amount=float(product_amount.price)*float(quantity)
        abc=Order(product_refer_id=request.POST["product_refer"],
                  customer_refer_id=request.POST["customer_refer"],
                  order_id=request.POST["order_id"],
                  quantity=request.POST["quantity"],
                  total=total_amount)
        abc.save()
        return redirect("/mysql/orderview/")
    return render(request,"order_add.html",data)


def order_view(request):
    data={
        "all_data":Order.objects.all()
    }
    return render(request,"order_view.html",data)

def order_update(request,id):
    selected=Order.objects.get(order_id=id)
    data={
        "orderform":Order_form(instance=selected)
    }
    if request.method=="POST":
        abc=Product.objects.get(id=request.POST["product_refer"])
        quantity=request.POST["quantity"]
        total_amount=float(abc.price)*float(quantity)
        xyz=Order(product_refer_id=request.POST["product_refer"],
                  customer_refer_id=request.POST["customer_refer"],
                  order_id=request.POST["order_id"],
                  quantity=request.POST["quantity"],
                  total=total_amount)
        xyz.save()
        return redirect("/mysql/orderview/")
    return render(request,"order_add.html",data)

def order_delete(request,id):
    selected=Order.objects.get(order_id=id)
    selected.delete()
    return redirect("/mysql/orderview/")
