
from multiprocessing import context
from re import X, template
from django.shortcuts import  render, redirect, HttpResponse
#from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.template import loader

from learner.forms import CreateUserForm
from .models import Course, Student

# def index(request):
# 	return render(request, 'mainapp/index.html')

def index(request):
  course = Course.objects.all()
#   template = loader.get_template('mainapp/index.html')
  context = {
    'course': course,
  }
  return render(request, 'index2.html', context)

def home(request):
  return render(request, 'home.html')

def succen(request):
  return render(request, 'succen.html')

def unsuccen(request):
  return render(request, 'unsuccen.html')

def enroll(request, id):
  mycourse = Course.objects.get(id=id)
  template = loader.get_template('enroll.html')
  context = {
    'mycourse' : mycourse, 
  }
  return HttpResponse(template.render(context, request))




def senroll(request, id):
  ekey = request.POST['userkey']
  course = Course.objects.get(id=id)
  if (ekey == course.enrollkey):
    new_user=request.user 
    new_user= User.objects.get(id=new_user.id)
    student= Student.objects.get(sid=new_user.id)
    student.edc.add(course)
    return redirect ("succen")
  else:
    return redirect ("unsuccen")







# def enrollkey(request, id):
#   x = request.POST['userkey']
#   course = Course.objects.get(id=id)
#   context = {
#     'course' : course, 
#   }
#   if x == course.enrollkey:
#     current_user = request.user
#     student= Student.objects.get(id=current_user.id)

#     student.enrolledcourses = course
#     return redirect ("succen")
#   else:
#     return redirect ("unsuccen")


def register(request):
  form = CreateUserForm()


  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      messages.info(request, "Thanks for registering. You are now logged in.")
      new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
      login(request, new_user)
      

      new_user = User.objects.get(id=new_user.id)
         
      member = Student(sid=new_user)
      member.save()
     
  context = {'form':form}
  
  return render(request, 'register.html',context)



def userlogin(request):
  if request.method=="POST":
        # Get the post parameters
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']

      user=authenticate(username= loginusername, password= loginpassword)
      if user is not None:
          login(request, user)
          messages.success(request, "Successfully Logged In")
          return redirect("home")
      else:
          messages.error(request, "Invalid credentials! Please try again")
          return redirect("login")
  return render (request,'login.html')

  # return HttpResponse("404- Not found")
# def senroll(request):
#   course=Course.objects.get(id=id)
#   key=request.POST.get('userkey')
#   user=request.user
#   if (key==course.enrollkey):
#     user.Student.enrolledcourses.add(course)
#     return redirect('home')
	
	
