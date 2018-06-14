#coding=utf-8
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    return render(request, 'Login/index.html')

def login(request):
    return render(request, 'Login/login.html')

def login_action(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        request.session['user'] = username
        return render(request, 'Login/index.html', {'message': "login sucess"})
    else:
        return render(request, 'Login/login.html', {'message': {'text':"用户名或密码错误！",'color':'red'}})

def register(request):
    return render(request, 'Login/register.html')

def reg_action(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    User.objects.create_user(username=username, password=password, email=email)
    return render(request, 'Login/login.html', {'message': {'text':"注册成功！",'color':'yellow'}})