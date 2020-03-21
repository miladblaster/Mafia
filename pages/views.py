from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import CustomUser, get_user, set_user_role, get_user2
from django.http import HttpResponse




def index(request):
    return render(request,'pages/index.html')

def register(request):
    if request.method== "POST" :
        #get values:
        username=request.POST['username']
        name=request.POST['name']
        password=request.POST['password']
        password2=request.POST['password2']
        #making sure passwords match:
        if password!=password2:
            messages.error(request,"Passwords don't match")
            return redirect ('register')
        
        elif password==password2:
            #username check:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,'This username already exists')
                return redirect ('register')
            else:
                user = CustomUser.objects.create_user(username=username, password=password,name=name)
                auth.login(request, user)
                messages.success(request, 'you are now logged in')
                return redirect ('index')
                # user.save()
                # messages.success(request,"you are now registered, please log in")
                # return redirect ('login')

    else:
        return render(request, 'pages/register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'you are now logged in')
            return redirect('index')
        else:
            messages.error(request,'Wrong credintials')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')



def dashboard(request):
    return render (request, 'pages/dashboard.html')

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request, "You are successfully logged out!")
        return redirect('index')

def day(request):
    playerno= CustomUser.objects.filter(group=request.user.group).count()
    names=[None]
    for i in range (1,playerno+1):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }

    return render (request,'pages/day.html',context)

def night(request):
    playerno= CustomUser.objects.filter(group=request.user.group).count()
    names=[None]
    for i in range (1,playerno+1):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }
    return render(request,'pages/night.html',context)


def wait(request):
    playerno= CustomUser.objects.filter(group=request.user.group).count()
    names=[None]
    for i in range (1,playerno+1):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }
    return render(request,'pages/wait.html',context)

def setup(request):
    playerno= CustomUser.objects.filter(group=request.user.group).count()
    names=[None]
    for i in range (1,playerno+1):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }
    return render (request, 'pages/setup.html',context)