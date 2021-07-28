from django.shortcuts import render,redirect 
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm
from .models import UserProfile
from home.models import *
from product.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 

# Create your views here.

def user(request):
    return HttpResponse('good')


def loginform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid username/password')
    
    profile=Profile.objects.get(pk=1)
    manufacturers=Manufacturers.objects.all()

    context={
        'profile': profile,
        'manufacturers':manufacturers,
    }

    return render(request, 'login.html', context)

def logoutfunc(request):
    logout(request)
    return redirect('loginform')

def registerform(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            myuser = form.save()
            p = UserProfile(user=myuser)
            p.first_name = myuser.first_name
            p.last_name = myuser.last_name
            p.save()
            login(request,myuser)
            return redirect('loginform')
        else:
                messages.warning(request,form.errors)
                return redirect('registerform')
    
    profile=Profile.objects.get(pk=1)
    manufacturers=Manufacturers.objects.all()

    context={
        'profile': profile,
        'manufacturers':manufacturers,
    }

    return render(request, 'register.html', context)