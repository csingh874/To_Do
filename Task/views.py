from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

@login_required(login_url="login")
def user_home(request):
    user_name = request.user
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = user_name
            fs.save()
            return redirect("home")

    tasks = user_Task.objects.filter(author__exact = user_name)
    context= {"form":form,"tasks":tasks}
    return render(request,"home.html",context)

@login_required(login_url="login")
def task_update(request,pk):
    task=user_Task.objects.get(id = pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form":form}
    return render(request,"update.html",context)

@login_required(login_url="login")
def task_delete(request,pk):
    item = user_Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("home")

    context = {"item":item}
    return render(request,"delete.html",context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                messages.info(request,"Username or Password is Incorrect")

        return render(request,"login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def user_register(request):

    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = UserFormCreation()
        if request.method == "POST":
            form = UserFormCreation(request.POST)
            if form.is_valid():
                form.save()
                return redirect("login")

        context = {"form":form}
        return render(request,"register.html",context)


@login_required(login_url="login")
def pass_change(request):
    form = PasswordChangingForm(user= request.user)
    if request.method == "POST":
        form = PasswordChangingForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form":form}
    return render(request,"changepassword.html",context)



