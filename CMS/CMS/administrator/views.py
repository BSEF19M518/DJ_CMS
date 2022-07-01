from django.shortcuts import render

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
