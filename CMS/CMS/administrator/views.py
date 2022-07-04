from django.shortcuts import render, redirect
from . forms import TeacherForm, UserForm
from teacher.models import Teacher

# Create your views here.


def home(request):
    
    context={'colors':['success',
                       'primary',
                       'warning',
                       'danger'
                       'secondary',
                       'info',
                       'dark']}
    return render(request,'administrator/home.html',context)


def add_teacher(request):
    
    if request.method == 'POST':
        teacherForm = TeacherForm(request.POST)
        userForm = UserForm(request.POST)
        
        if teacherForm.is_valid() and userForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password('cms123')
            user.save()
            
            teacher = teacherForm.save(commit=False)
            teacher.user=user
            teacher.save()
            
            return redirect('administrator:home')
        
    teacherForm = TeacherForm()
    userForm = UserForm()
    
    context = {'user_form':userForm, 'teacher_form':teacherForm}
    return render(request, 'administrator/add_teacher.html', context)

def update_teacher(request,pk):
    
    teacher = Teacher.objects.get(id=pk)
    user=teacher.user    
    
    if request.method == 'POST':
        teacherForm = TeacherForm(request.POST,instance=teacher)
        userForm = UserForm(request.POST,instance=user)
        
        if teacherForm.is_valid() and userForm.is_valid():
            userForm.save()
            teacherForm.save()
            
            return redirect('administrator:view_teachers')
    
    teacherForm = TeacherForm(instance=teacher)
    userForm = UserForm(instance=user)
    
    context = {'user_form':userForm, 'teacher_form':teacherForm}
    return render(request, 'administrator/add_teacher.html', context)

def delete_teacher(request,pk):
    
    teacher = Teacher.objects.get(id=pk)
    user=teacher.user
    print(user.username)    
    
    user.delete()
    teacher.delete()
    return redirect('administrator:view_teachers')
    
def view_teachers(request):
    teachers= Teacher.objects.all()
    context = {'teachers':teachers}
    return render(request, 'administrator/view_teachers.html', context)