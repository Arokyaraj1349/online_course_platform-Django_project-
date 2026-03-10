from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test 
from .models import Course


# Create your views here.
def admin_check(user): 
    return user.is_superuser 
def index(request):
    courses = Course.objects.all() 
    return render(request,"index.html",{'courses': courses} )

def adminpage(request):
    courses = Course.objects.all() 
    users = User.objects.all() 
    return render(request,"admin.html",
    {"courses": courses, 
     "users": users})
def loginview(request):
    if request.method=="POST":
        name= request.POST.get("username")
        password_=request.POST.get("password")
        User=authenticate(
            request,
            username=name,
            password=password_
        )
        if User:
            login(request,User)
            if User.is_superuser:
                return redirect('adminpage')
            else:
                return redirect('home')
        else:
            return redirect(request,'home')
    
    return render(request,"login.html",{'error': 'Invalid credentials'})
def signuppage(request):
    if request.method =='POST':
        name=request.POST.get('username')
        password_=request.POST.get('password')
        email_=request.POST.get('emailid')
        u=User.objects.create_user(
            username=name,
            password=password_,
            email=email_
        )
        u.save()
        login(request,u)
        return redirect('home')
    return render(request,"signup.html")
def logout_view(request): 
    logout(request) 
    return redirect("home")
# ADD COURSE 
@login_required(login_url='admin') 
@user_passes_test(admin_check) 
def add_course(request): 
    if request.method == "POST": 
        title = request.POST.get("title") 
        description = request.POST.get("description") 
        price = request.POST.get("price") 
        image = request.FILES.get("image") 

        Course.objects.create( 
            title=title, 
            description=description, 
            price=price, 
            image=image 
        ) 
        return redirect("adminpage") 
    return render(request,"addcourse.html")
@login_required(login_url='home') 
@user_passes_test(admin_check) 
def delete_course(request, id): 
    course = get_object_or_404(Course, id=id) 
    course.delete() 
    return redirect("adminpage") 
def update_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.method == "POST":
        course.title = request.POST.get("title")
        course.description = request.POST.get("description")
        course.price = request.POST.get("price")

        if request.FILES.get("image"):
            course.image = request.FILES.get("image")

        course.save()
        return redirect('adminpage')   # redirect to admin page

    return render(request, "update.html", {"course": course})