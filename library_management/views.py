from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import  authenticate
from django.contrib.auth import  login
from library_management.models import Book

# Create your views here.

def index(request):
    # if User.is_authenticated:
    #     return render (request, 'index.html', {'first_name':User.first_name})
    # else:
    return render (request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('sinup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('sinup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('sinup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('sinup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('sinup', {})
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        return redirect('sinup')   
    else:
         return render(request, 'sinup.html')

        

def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username = username , password=password)
        
        if user is not None:
            login(request, user)
            return redirect ('home')
        # elif User.is_authenticated:
        #     return HttpResponse('You have already sign in')         
        else:
            messages.error(request, "wrong credentials")
            return redirect ("signin")
           
    return render(request, 'signin.html')
    
def details(request):
    return render(request, 'details.html')

def logout(request):
        auth_logout(request)
        return redirect('home')

def books(request):
    books = Book.objects.all()
    return render (request, 'books.html' ,{'books': books})


def add_book(request):
    pass