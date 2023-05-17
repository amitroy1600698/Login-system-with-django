from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            return HttpResponse("Confirm password is not match")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
        
            my_user.save()
        
            return redirect('signin')
           
    return render(request, 'signup.html')

def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        
        user = authenticate(request,username=username,password = pass1)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('signin')
            
    
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')
