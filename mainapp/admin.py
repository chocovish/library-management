from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,Book
from django import forms

BaseUserAdmin.fieldsets += ('Custom fields set', {'fields': ('phone', 'roll','stream','year','verified')}),

admin.site.register(User,BaseUserAdmin)


admin.site.register(Book)
#admin.site.register(User)