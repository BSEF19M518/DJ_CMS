from re import M
from django.db import models
from django.contrib.auth import get_user_model

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

SHIFT_CHOICES = (
    ('M','Morning'),
    ('A','Afternoon'),
)

SEASON_CHOICES = (
    ('S','Spring'),
    ('F','Fall'),
)

# SEMESTER_CHOICES = (
#    ('1','1'),
#    ('2','2'),
#    ('3','3'),
#    ('4','4'),
#    ('5','5'),
#    ('6','6'),
#    ('7','7'),
#    ('8','8'),
# )


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    profile_picture=models.ImageField(null=True, blank=True)
    rollNumber= models.CharField(primary_key=True,max_length=12)
    homeAddress= models.CharField(max_length=100,null=True, blank=True)
    telephone=models.CharField(max_length=15,null=True, blank=True)
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True, blank=True)
    dateOfBirth= models.DateField(null=True, blank=True)
    major= models.CharField(max_length=2,choices=MAJOR_CHOICES,null=True, blank=True)
    batch=models.ForeignKey('Batch',on_delete=models.SET_NULL,null=True)
    shift = models.CharField(max_length=1, default='M', choices=SHIFT_CHOICES)
        
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Student'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class SessionInfo(models.Model):
    season= models.CharField(max_length=1,choices=SEASON_CHOICES)
    year= models.PositiveIntegerField(default=2000,null=True)

    def __str__(self):
        return f'Session(Season: {self.season}, year: {self.year})'

class Batch(models.Model):
     sessionInfo = models.ForeignKey(SessionInfo, on_delete=models.SET_NULL, null=True)
     pass_out= models.BooleanField(default=False,blank=True,null=True)     
     semester= models.PositiveIntegerField(default=1,null=True)
     def __str__(self):
        return f'Batch(Session: {self.sessionInfo} | current_semester: {self.semester})'
