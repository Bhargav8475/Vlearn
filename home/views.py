from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as authlogin
from django.contrib.auth.decorators import login_required


# Create your views here.
def req(request):
    return render(request, 'VLearn.html')
@login_required
def homereq(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
            uname = request.POST.get('uname')
            passw = request.POST.get('passw')
            user = authenticate(request,username=uname, password=passw)
            if user is not None:
                authlogin(request, user)
                return redirect('home')
            else:
                return HttpResponse('errorasdasdasda')
    return render(request, 'login.html', {})

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        passw = request.POST.get("passw")
        new_user = User.objects.create_user(uname,email,passw)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        return redirect('login')
        
    return render(request, 'SignUp.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login')