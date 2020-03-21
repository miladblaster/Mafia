from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, name, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """

        user = self.model(username=username,name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, name, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, name, password, **extra_fields)

    #doesnt seem to work for some reason
    def get_user(x):
        try:
            return CustomUser.objects.get(is_alive=True,number=x)
        except CustomUser.DoesNotExist:
            return None

    def set_user_role(y,x):
        try:
            return CustomUser.objects.filter(number=y).update(role=x)
        except CustomUser.DoesNotExist:
            return None


    
