from django.db import models
from datetime import timedelta
 
 #MODELS FOR COURSE SUBJECT
class Subjects(models.Model):
    subjectname = models.CharField(max_length=30)
    subjectImage = models.ImageField(upload_to='subjectimages',) #upload to media folder
    subjectDescription = models.TextField()


    def __str__(self):
        return self.subjectname


#controlling pluralization of  subject 
    class Meta:
        verbose_name = 'Subjects'
        verbose_name_plural = 'Subjects'

      

#MODELS FOR COURSES
class Course(models.Model):
    courseSubject = models.ForeignKey(Subjects, on_delete=models.CASCADE,name="course", verbose_name="Course Subject")#relationship for subjects to course
    courseImage = models.ImageField(upload_to='subjectimages',help_text="image size 100 by 100",verbose_name="Course Image")
    courseName = models.CharField(max_length=100,verbose_name="Course Name")
    coursePrice = models.PositiveIntegerField(help_text='Price in dollars',verbose_name="Course Price")
    courseDuration = models.DurationField(default=timedelta(hours=5,minutes=20),verbose_name="Course Duration")

#made some db migrations

    def __str__(self):
        return self.courseName
 








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