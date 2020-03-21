from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('day',views.day,name='day'), #This is step 2. There needs to be an HTML for this
    path('night',views.night,name='night'), #This is step 3. make an HTML for it.
    path('wait',views.wait,name='wait'), #This is where they go before day
    path('setup',views.setup,name='setup'), #This is where they set the groups

]
