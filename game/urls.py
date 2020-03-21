from django.urls import path
from . import views

urlpatterns=[
    path('game',views.game, name='game'),
    path('assign', views.assign, name='assign'), #this is step 1 to begin game. should be in dashboard
    path('lynch', views.lynch,name='lynch'),
    path('target',views.target,name='target'),
    path('heal',views.heal,name='heal'),
    path('shoot',views.shoot,name='shoot'),
    path('inspect',views.inspect,name='inspect'),
    path('make_group',views.make_group,name='make_group'),
    path('add_to_group',views.add_to_group,name='add_to_group'),
    path('gpname',views.gpname,name='gpname'),
    path('select_roles',views.select_roles,name='select_roles'),
    # path('day',views.day,name='day'), #This is step 2. There needs to be an HTML for this
    # path('night',views.night,name='night'), #This is step 3. make an HTML for it.
]