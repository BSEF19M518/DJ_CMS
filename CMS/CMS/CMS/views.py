from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'base.html')

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        print('hehs')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Returns a user object
        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('administrator:home')
        
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)