from django.contrib import admin
from django.urls import path
from .views import home,add_teacher,view_teachers, update_teacher, delete_teacher
app_name='administrator'

urlpatterns = [
    path('', home, name="home"),
    path('add_teacher/', add_teacher, name="add_teacher"),
    path('view_teachers/', view_teachers, name="view_teachers"),
    path('update_teacher/<str:pk>/', update_teacher, name="update_teacher"),
    path('delete_teacher/<str:pk>/', delete_teacher, name="delete_teacher"),
]