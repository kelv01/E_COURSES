from django.contrib import admin

# importing all models here.
from .models import *


#for extra userx to view more details in the admin like price n name,
#passing class to the  admin.site reg
class CourseAdmin(admin.ModelAdmin):
    list_display = ["courseName","coursePrice","courseDuration"]
    list_editable = ["coursePrice"]

# Register your models here.
admin.site.register(Course,CourseAdmin)
admin.site.register(Subjects)

