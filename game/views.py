from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint
from django.contrib import messages, auth
from django.contrib.auth.models import User
from users.models import CustomUser,get_user,set_user_role #Have to import them
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField

roleslist=[]
#Buttons:________________________________________________________
#Get group name and usernames and enter their usernames.
def make_group(request):
    groupname=request.POST['groupname']
    if CustomUser.objects.filter(group=groupname).exists():
        messages.error(request,'This groupname already exists')
    else:
        CustomUser.objects.filter(username=request.user).update(group=groupname,number=1)

        messages.success(request,'Group created!')
    return render(request, 'pages/setup.html')

#Adding people:
def add_to_group(request):
    username=request.GET['username']
    CustomUser.objects.filter(username=username).update(group=request.user.group)
    gn=CustomUser.objects.filter(group=request.user.group).count()
    CustomUser.objects.filter(username=username).update(number=gn)
    gn=gn+1
    messages.success(request,'user Added!')
    return render(request, 'pages/setup.html')

#To verify before playing, please enter your group name:
def gpname(request):
    groupname=request.POST['groupname']
    if CustomUser.objects.filter(username=request.user.username,group=groupname).exists():
        messages.success(request,"You're good to go!")
        return render (request, 'pages/dashboard.html')
    else:
        messages.error(request,"You haven't been added to this group yet. please ask your leader to do so")
        return render (request, 'pages/dashboard.html')


#Role choices:
def select_roles(request):
    role1,role2,role3,role4,role5=None,None,None,None,None
    global roleslist
    
    role1=request.GET['role1']
    role2=request.GET['role2']
    role3=request.GET['role3']
    role4=request.GET['role4']
    # role5=request.GET['role5']
        
    roleslist=[role1,role2,role3,role4,role5]
    return render (request, 'pages/setup.html')



#Role assignment:
def assign(request):
    global roleslist
    playerno=int(request.POST['playerno'])

    #Making everyone alive:
    
    for i in range (1,playerno+1):
        CustomUser.objects.filter(number=i,group=request.user.group).update(is_alive=True)

    #Randoming roles
    
    x1,x2,x3,x4,x5,x6,x7 = 0,0,0,0,0,0,0
    xa,xb,xc,xd,xe,xf,xg = "","","","","","",""
    for i in range (1,1000):
        r1=randint(1,playerno)
        if r1==1:
            x1=x1+1
        if r1==2:
            x2=x2+1
        if r1==3:
            x3=x3+1
        if r1==4 and playerno>=4:
            x4=x4+1
        if r1==5 and playerno>=5:
            x5=x5+1
        if r1==6 and playerno>=6:
            x6=x6+1
        if r1==7 and playerno>=7:
            x7=x7+1
        
    listx=[x1,x2,x3,x4,x5,x6,x7]
    listx.sort(reverse=True)
    listroles=roleslist
    # listroles=['Mafia','Doctor','Sniper','Detective','Joker','Silencer','Angel']
    mixlist=dict(zip(listx,listroles))
    
    # groupname = CustomUser.objects.filter(group=request.user.group,number=1).values_list('group', flat=True)
    # m=groupname
    set_user_role(request,1,mixlist[x1])
    set_user_role(request,2,mixlist[x2])
    set_user_role(request,3,mixlist[x3])
    set_user_role(request,4,mixlist[x4])
    set_user_role(request,5,mixlist[x5])
    # set_user_role(request,6,mixlist[x6])    
    # set_user_role(request,7,mixlist[x7])


    names=[None]
    # playerno= CustomUser.objects.filter(group=request.user.group).count()
    for i in range (1,playerno):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }
    #Making detective message disappear:
    CustomUser.objects.filter(group=request.user.group).update(message='')
    #Making sure they go to day.
    CustomUser.objects.filter(group=request.user.group).update(has_lynched=False)


    #Getting everyone permission to begin:
    CustomUser.objects.filter(group=request.user.group).update(can_play=True)
    return render(request,'pages/day.html',context)


def lynch(request):
    playerno= CustomUser.objects.filter(group=request.user.group).count()
    names=[None]
    for i in range (1,playerno+1):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }
    lynch=request.POST['lynch']
    if lynch is not None:
        CustomUser.objects.filter(username=lynch).update(is_alive=False)

        #Need to update the list after lynch:
        playerno= CustomUser.objects.filter(group=request.user.group).count()
        names=[None]
        for i in range (1,playerno+1):
            names.append(get_user(request,i))

        play=dict(zip(names,names))
        context={
            'play': play
        }
        #making sure they go to night afterwards
        CustomUser.objects.filter(group=request.user.group).update(has_lynched=True)
        return render (request,'pages/night.html', context)
    else:
        CustomUser.objects.filter(group=request.user.group).update(has_lynched=True)
        return render (request,'pages/night.html', context)




#Role inputs:

#Mafia:
def target(request):
    global target
    target=request.POST['target']

    return render (request,'pages/wait.html')

#Doctor:
def heal(request):
    global heal
    heal=request.POST['heal']

    return render (request,'pages/wait.html')


#Sniper:
def shoot(request):
    global shoot
    shoot=request.POST['shoot']

    return render (request,'pages/wait.html')


#Detective:
def inspect(request):
    global inspect
    inspect=request.POST['inspect']

    return render (request,'pages/wait.html')


#Calculations:
def game(request):
    
    #Mafia and doctor:
    if heal != target:
        CustomUser.objects.filter(username=target).update(is_alive=False)
    
    #Sniper:
    if shoot is not None:
        if CustomUser.objects.filter(name=shoot,role='Mafia').exists():
            CustomUser.objects.filter(name=shoot).update(is_alive=False)
        else:
            CustomUser.objects.filter(role='Sniper').update(is_alive=False)
    
    #Detective:
    xx=None
    if CustomUser.objects.filter(role='Mafia',group=request.user.group).exists():
        xx=CustomUser.objects.filter(role='Mafia',group=request.user.group).get()

    if inspect == xx:
        CustomUser.objects.filter(role='Detective').update(message ='Good Guess! The person you investigated is indeed Mafia!')
    else:
        CustomUser.objects.filter(role='Detective').update(message ='Wrong Guess! The person you investigated is NOT Mafia! ')



    #Loading it to the list:
    names=[None]
    playerno= CustomUser.objects.filter(group=request.user.group).count()
    for i in range (1,playerno+1):
        names.append(get_user(request,i))

    play=dict(zip(names,names))
    context={
        'play': play
    }
    #Making sure they go to day afterwards
    if CustomUser.objects.filter(has_lynched=False,is_alive=True,group=request.user.group).count() == CustomUser.objects.filter(is_alive=True,group=request.user.group).count():
        return render(request,'pages/day.html', context)
    else:
        return render (request, 'pages/wait.html')





