from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'image', 'email', 'address', 'phone', 'city', 'country']
    readonly_fields = ['username', 'first_name', 'last_name',  'email', 'address', 'phone', 'city', 'country', 'zipcode', 'state', 'date']


# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)
