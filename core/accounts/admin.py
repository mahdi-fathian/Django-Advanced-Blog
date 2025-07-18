from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'is_active', 'is_staff', 'is_superuser', 'is_verified')

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser', 'is_verified', 'date_joined', 'last_login')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_verified', 'date_joined')
    search_fields = ('email',)
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login', 'created_date', 'updated_date')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_verified', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'created_date', 'updated_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_verified', 'is_superuser')
        }),
    )


admin.site.register(User, CustomUserAdmin)
























