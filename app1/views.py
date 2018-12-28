from django.shortcuts import render
from django.db.models import Q
from .models import Course
from  django.contrib import messages
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
    return render(request,'app1/home.html')