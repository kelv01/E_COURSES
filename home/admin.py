from django.contrib import admin

# importing all models here.
from .models import *

# Register your models here.
admin.site.register(Course)
admin.site.register(Subjects)
