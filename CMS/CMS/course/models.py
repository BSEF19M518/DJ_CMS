from django.db import models
from student.models import Student
from teacher.models import Teacher
# Create your models here.

COURSE_CHOICES = (
    ('T','Theory'),
    ('L','Lab')
)

class Course(models.Model):
    
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    credit_hrs = models.FloatField()
    course_type = models.CharField(max_length=1, choices=COURSE_CHOICES)
    
    
    def __str__(self):
        return self.title

class EnrolledCourses(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL,null=True)
    course=models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True)
    semester = models.PositiveIntegerField(default=1)

