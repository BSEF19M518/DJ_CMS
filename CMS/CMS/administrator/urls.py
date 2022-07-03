from django.contrib import admin
from django.urls import path
from .views import home,add_teacher,view_teachers
app_name='administrator'

urlpatterns = [
    path('', home, name="home"),
    path('add_teacher', add_teacher, name="add_teacher"),
    path('view_teachers', view_teachers, name="view_teachers"),
]