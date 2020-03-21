from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active','role','is_alive','number','group',)
    list_filter = ('username', 'is_staff', 'is_active','role','is_alive','number','group',)
    fieldsets = (
        (None, {'fields': ('username','name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Game_status', {'fields': ('role','side','is_alive','number','has_lynched','group','can_play','message')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'name', 'password1', 'password2', 'is_staff',)}
        ),
    )
    search_fields = ('username','name','is_alive','group')
    ordering = ('username','name','is_alive','group')


admin.site.register(CustomUser, CustomUserAdmin)