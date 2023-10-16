from django.contrib import auth , messages
from django.contrib.auth import authenticate , login
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Department,Purpose
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
# Create your views here.
def register(request):
    if request.method == 'POST':
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            cpassword=request.POST['cpassword']
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save();
            print ( "user created" )
            return redirect('signin')
    # elif user.objects.filter(username=username).exists():
    #         messages.info(request,"username already taken")
    #         return redirect("register")
    # elif user.objects.filter(email=email).exists():
    #         messages.info(request,"email already exists")
    #         return redirect("register")
    else:
      return render(request,"registration.html")



def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        myuser=auth.authenticate(username=username,password=password)
        myuser.save();
        if myuser is not None:
            auth.login(request,myuser)
            return redirect('dataform')
        else:
            messages.info("Invalid credentials")
            return redirect('signin')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
def dataform(request):
    # if request.method == "POST":
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     if User.is_valid():
      return render(request,"dataform.html")

def allCourse(request):
      links=Department.objects.all()
    # d_page = None
    # courses = None
    # if(d_slug != None):
    #     d_page=get_object_or_404(Department, slug=d_slug)
    #     courses = Course.objects.all().filter(department=d_page, available=True)
    # else:
    #     courses = Course.objects.all().filter(available=True)
     # paginator = Paginator(courses, 6)
     # try:
     #    page = int(request.GET.get('page', 1))
     # except:
     #    page = 1
     # try:
     #    courses=paginator.page(page)
     # except (EmptyPage,InvalidPage):
     #    courses=paginator.page(paginator.num_pages)
      return render(request,"home.html",{'links':links})

#
def department(request,slug):
    department=Department.objects.get(slug=slug)
    print(department)
    return render(request,"department.html",{'department':department})

def purpose(request,slug):
    purpose=Purpose.objects.get(slug=slug)
    print(purpose)
    return render(request,"purpose.html",{'purpose':purpose})
def item(request,slug):
    item=Purpose.objects.get(slug=slug)
    return(request,"confirm.html",{'item':item})




