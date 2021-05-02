from typing import ContextManager
from django.db.models.query import prefetch_related_objects
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group,User

def landing(request):
    if request.user.is_authenticated:
        usrauthstts = 'True'
    else:
        usrauthstts = 'False'
    
    context={
        'auth':usrauthstts
    }

    return render(request,'index.html',context)

def loginpage(request):
    context={
    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            # print(str(user.groups.all()),user,Group.objects.get(name='Murid'))
            murid = Group.objects.get(name='Murid') in user.groups.all()  
            guru = Group.objects.get(name='GuruMapel') in user.groups.all()  
            print(murid,guru)
            if murid:
                return redirect('dashboardmurid:dashboardmurid')
            if guru:
                return redirect('dashboardguru:dashboardguru')

    return render(request,'login.html',context)

@login_required
def logoutpage(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("landing")