from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            email=request.POST['email'],
            password=password
        )
        log = authenticate(request, username=username, password=password)
        login(request, log)
        return redirect('home')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured!')
            return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
