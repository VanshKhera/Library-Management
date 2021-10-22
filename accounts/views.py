from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.user.is_authenticated:    
        return redirect('/')    
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            form = RegisterForm()
        return render(request, 'register.html', {"form" : form})

def Login(request):
    if request.user.is_authenticated:    
        return redirect('/')    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.warning(request, "Username or password is incorrect")
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')