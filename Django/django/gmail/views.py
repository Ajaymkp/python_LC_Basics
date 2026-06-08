from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random
a=""
def email_sending(request):
    global a
    if request.method=="POST":
        t_mail=request.POST["recieve"]
        sub=request.POST["subject"]
        # msg=request.POST["content"]

        a=""
        for i in range(4):
            a=a+str(random.randint(0,9))
            msg=f"otp is {a}"

        send_mail(
            sub,
            msg,
            "settings.EMAIL_HOST_USER",
            [t_mail],fail_silently=False
        )
        return redirect("/gmail/action/")
    return render(request, 'gmail.html')
x=""
def action(request):
    global x
    if request.method=="POST":
        print(request.POST)
        x=request.POST["n"]
        return redirect("/gmail/verify/")
    return render(request,"action.html")


def verification(request):
    data={
        "y":x,
        "b":a
    }
    return render(request,"verify.html",data)
