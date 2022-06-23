from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
)

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True)
    profile_picture=models.ImageField(null=True, blank=True)
    homeAddress= models.CharField(max_length=100,null=True, blank=True)
    telephone=models.CharField(max_length=15,null=True, blank=True)
    gender= models.CharField(max_length=1,choices=GENDER_CHOICES,null=True, blank=True)
    dateOfBirth= models.DateField(null=True, blank=True)
    designation= models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'