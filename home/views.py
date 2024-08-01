from django.shortcuts import render
from .models import Course, Subjects # importing models of course n subject therefore identify the view that gives us the two
from django.db import models
 


def index(reqest):
    return render(reqest, 'index.html')


def course(reqest):
    all_courses = Course.objects.all() # this is how you query the database for all the courses

    #all_subjects = Subjects.objects.all()

#adding count for related courses
    all_subjects = Subjects.objects.annotate(course_count=models.Count('course'))
    

    context = {"allcourses":all_courses,"allsubjects":all_subjects}
 

    return render(reqest, 'course.html',context)#allcourses/subjects dictionary


def teacher(reqest):
    return render(reqest, 'teacher.html')


def about(reqest):
    return render(reqest, 'about.html')


def blog(reqest):
    return render(reqest, 'blog.html')


def contact(reqest):
    return render(reqest, 'contact.html')


def single(reqest):
    return render(reqest, 'single.html')