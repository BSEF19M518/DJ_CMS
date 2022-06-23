from django.contrib import admin
from course.models import Course,EnrolledCourses,Attendance
# Register your models here.

admin.site.register(Course)
admin.site.register(EnrolledCourses)
admin.site.register(Attendance)