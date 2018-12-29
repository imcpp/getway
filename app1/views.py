from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Course
from  django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



# Create your views here.
def home(request):
    return render(request,'app1/home.html')

def allcourses(request):
    allcourses=Course.objects.all()
    return render(request,"app1/allcourses.html",{"allcourses":allcourses})
def search(request):
    if request.method=='POST':
        search=request.POST['srh']

        if search:
            match=Course.objects.filter(Q(course_name__icontains=search) )

            if match:
                return render(request,"app1/allcourses.html",{"allcourses":match})

            else:
                 messages.error(request,'SORRY!!!THIS COURSE IS NOT AVAILABLE !!! ')
                 return render(request,'app1/allcourses.html')

        else:
            return HttpResponseRedirect('')
            return render(request,'app1/home.html')

    return render(request,'app1/home.html')

def login(request):

    if request.method=='GET':
           return render(request,'app1/home.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)

            return redirect('home')
        else:
            return render(request,'app1/home.html',{'error':'username or password is incorrect'})

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')

def signup(request):
        if request.POST['password']==request.POST['cpassword'] :
                try:
                    user=User.objects.get(username=request.POST['username'])
                    return render(request,'app1/home.html',{'error':'Username already exist !! Please choose a different one :'})
                except:
                    user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                    #auth.login(request,user)
                    #return HttpResponse('<h1>Home Page<h1>')
                    #return redirect('home')
                    return render(request,'app1/home.html',{'error':'signup successful !!'})

        else:
            return render(request,'app1/home.html',{'error':'password does not match'})
