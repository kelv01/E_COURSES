from django.shortcuts import render

def index(reqest):
    return render(reqest, 'index.html')


def course(reqest):
    return render(reqest, 'course.html')


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