from django.contrib import admin

# Register your models here.
from .models import djangoClasses

#calling djangoClasses
admin.site.register(djangoClasses)