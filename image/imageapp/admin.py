from django.contrib import admin
from imageapp.models import *


# @admin.register(Profile)
# class ProfileModelAdmin(admin.ModelAdmin):
#     list_display = ['id','name','email','dob','state','gender','location','pimage','rdoc']

admin.site.register(Photo) 