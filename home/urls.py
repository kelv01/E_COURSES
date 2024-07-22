from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('course/', views.course,name='course'),
    path('teacher/', views.teacher,name='teacher'),
    path('contact/', views.contact,name='contact'),
    path('blog/', views.blog,name='blog'),
    path('single/', views.single,name='single'),
]
