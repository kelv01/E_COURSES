from django.db import models
from datetime import timedelta
 
 #MODELS FOR COURSE SUBJECT
class Subjects(models.Model):
    subjectname = models.CharField(max_length=30)
    subjectImage = models.ImageField(upload_to='subjectimages',) #upload to media folder
    subjectDescription = models.TextField()
 

#MODELS FOR COURSES
class Course(models.Model):
    courseSubject = models.ForeignKey(Subjects, on_delete=models.CASCADE,name="course")#relationship for subjects to course
    courseImage = models.ImageField(upload_to='subjectimages')
    courseName = models.CharField(max_length=100)
    coursePrice = models.PositiveIntegerField(help_text='Price in dollars')
    courseDuration = models.DurationField(default=timedelta(hours=5,minutes=20))

#made some db migrations








"""

#gender drop down
genderInstance =(
    ('Male', 'Male')
    ('Female', 'Female')
    ('Other', 'Other')
)
# some of the  models used to capture in django. 
class UserInformation(models.Model):
    first_name = models.CharField(max_length=30)
    user_story =models.TextField(null=True,blank=True)
    ProfilePic = models.ImageField(upload_to='profilepics')
    DateOfBirth = models.DateField()
    DateOfRegistration = models.DateTimeField(auto_now_add=True)  
    email = models.EmailField(max_length=50)
    useResume = models.FileField(upload_to='resumes')
    salary = models.PositiveIntegerField()
    height = models.FloatField()
    gender = models.CharField(choices=genderInstance, max_length = 30)
    isActive = models.BooleanField(default=True)"""