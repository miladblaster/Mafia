from django.contrib.auth.models import User
from users.models import CustomUser, get_user, set_user_role
from django.contrib import messages, auth
from users.managers import CustomUserManager

#All players:
# m=""
# g= get_users_for_group(m)

# players={
#     m:m
# }



# #Alive players:
# i1,i2,i3,i4='','','',''
# p=4
# m='m'
# i1=get_user(p,m)
# i2=get_user(p-1,m)
# i3=get_user(p-2,m)
# i4=get_user(p-3,m)

# player_choices= {
#     #The None makes all the other dead people None:None and makes them go away

#     None:None,
#     get_user(p,m):get_user(p,m),
#     get_user(p-1,m):get_user(p-1,m),
#     get_user(p-2,m):get_user(p-2,m),
#     get_user(p-3,m):get_user(p-3,m),
# }


