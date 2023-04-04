from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Course, Script

# Register your models here.

admin.site.register(Course)
admin.site.register(Script)
admin.site.unregister(Group)
