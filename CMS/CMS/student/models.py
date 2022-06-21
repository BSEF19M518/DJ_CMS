from django.db import models
from django.contrib.auth import get_user_model
from course.models import Course

# Create your models here.

User = get_user_model()


GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
)

MAJOR_CHOICES = (
    ('SE','Software Engineer'),
    ('CS','Computer Science'),
    ('IT','Information Technology'),
)

SECTION_CHOICES = (
    ('M','Morning'),
    ('A','Afternoon'),
)

class Student(User):
    profile_picture=models.ImageField(null=True, blank=True)
    rollNumber= models.CharField(max_length=12)
    homeAddress= models.CharField(max_length=100,null=True, blank=True)
    telephone=models.CharField(max_length=15,null=True, blank=True)
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True, blank=True)
    dateOfBirth= models.DateField(null=True, blank=True)
    major= models.CharField(max_length=2,choices=MAJOR_CHOICES,null=True, blank=True)
    batch_year= models.IntegerField(default=0,null=True, blank=True)
    section= models.CharField(max_length=1,choices=SECTION_CHOICES,null=True, blank=True)
    courses=models.ManyToManyField(Course, null=True,blank=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Student'

