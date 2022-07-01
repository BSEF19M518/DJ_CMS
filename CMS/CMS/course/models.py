from cmath import inf
from django.db import models
from student.models import Student, Batch,SessionInfo
from teacher.models import Teacher
# Create your models here.

COURSE_CHOICES = (
    ('T','Theory'),
    ('L','Lab')
)

ATTENDANCE_CHOICES = (
    ('A','Absent'),
    ('P','Present'),
    ('L','Leave'),
    ('D', 'Delay'),
)

SHIFT_CHOICES = (
    ('M','Morning'),
    ('A','Afternoon'),
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
    courseEnrolled = models.ForeignKey('OfferedCourse', on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return f'Student: {self.student } enrolled in {self.courseEnrolled}'



class OfferedCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL,null=True)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True)
    sessionInfo= models.ForeignKey(SessionInfo, on_delete=models.SET_NULL, null=True)
    shift = models.CharField(max_length=1, default='M', choices=SHIFT_CHOICES)

    def __str__(self):
        return f'Batch: {self.batch } | Course: {self.course.title} | Teacher: {self.teacher} | SessionInfo: {self.sessionInfo} | Shift: {self.shift}'


class Attendance(models.Model):
    courseInfo = models.ForeignKey(EnrolledCourses, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=1,choices=ATTENDANCE_CHOICES)

    def __str__(self):
        return f'Student: {self.courseInfo.student} | Date: {self.date} | Status: {self.status}'

class CourseActivity(models.Model):
    name = models.CharField(max_length=15)
    weightage = models.FloatField()
    offered_course = models.ForeignKey(OfferedCourse, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Activity: {self.name} | Weight: {self.weightage} | Offered: {self.offered_course}"
class CourseActivityItem(models.Model):
    name = models.CharField(max_length=15)
    activity = models.ForeignKey(CourseActivity, on_delete=models.SET_NULL, null=True)
    total = models.FloatField()
    obtained = models.FloatField()
    
    def __str__(self):
        return f"Name: {self.name} | Activity: {self.activity}, Total: {self.total}"
     
class GradeBook(models.Model):
    course_activity_item = models.ForeignKey(CourseActivityItem, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL,null=True)
    obtained = models.FloatField()
    
    def __str__(self):
        return f"course_activity_item: {self.course_activity_item} || Student: {self.student} || Marks obt: {self.obtained} || "