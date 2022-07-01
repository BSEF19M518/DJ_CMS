from django.contrib import admin
from course.models import (Course,EnrolledCourses,
                           Attendance,OfferedCourse,
                           CourseActivity,CourseActivityItem,
                           GradeBook)
# Register your models here.

admin.site.register(Course)
admin.site.register(EnrolledCourses)
admin.site.register(Attendance)
admin.site.register(OfferedCourse)
admin.site.register(CourseActivity)
admin.site.register(CourseActivityItem)
admin.site.register(GradeBook)
