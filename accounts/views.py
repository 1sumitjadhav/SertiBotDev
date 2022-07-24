from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .forms import StudentSignUpForm,universitySignUpForm

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request, 'register.html')


class student_register(CreateView):
    model = User  
    form_class = StudentSignUpForm
    template_name= 'student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('validate')

class university_register(CreateView):
    model = User  
    form_class = universitySignUpForm
    template_name= 'university_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

def login_user(request):
    if request.user.is_authenticated:
        print("User is logged in :)")
        print(f"Username --> {request.user.username}")
        return redirect('../validate')
    else:
        print("User is not logged in :()")
    
        if request.method=='POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None :
                    login(request,user)
                    return redirect('../validate')
                else:
                    messages.error(request,"Invalid username or password")
            else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logout_user(request):
    logout(request)
    return redirect('index')