from django.db import models
 
class Subjects(models.Model):
    subjectname = models.CharField(max_length=30)
    subjectImage = models.ImageField(upload_to='subjectimages',)
 


class Course(models.Model):
    pass


class Teachers(models.Model):
    pass














"""genderInstance =(
    ('Male', 'Male')
    ('Female', 'Female')
    ('Other', 'Other')
)
# Create your models here.
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