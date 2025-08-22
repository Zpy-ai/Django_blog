from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'blog/login.html', {'error': '用户名或密码错误'})
    else:
        return render(request, 'blog/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # 检查用户名是否已存在
        if User.objects.filter(username=username).exists():
            return render(request, 'blog/register.html', {'error': '用户名已存在'})
        
        # 检查邮箱是否已存在
        if User.objects.filter(email=email).exists():
            return render(request, 'blog/register.html', {'error': '邮箱已被注册'})
        
        # 创建用户
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # 登录用户
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'blog/register.html')
