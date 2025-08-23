# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import Post, UserProfile
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
import markdown

def post_list(request):
    posts_list = Post.objects.order_by('-created_at')
    # 对每篇文章的内容进行Markdown处理
    for post in posts_list:
        post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    paginator = Paginator(posts_list, 9)  # 每页显示5篇文章
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page参数不是一个整数，返回第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果page参数超出范围，返回最后一页
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    # 获取最新的5篇文章，并确保包含作者信息
    latest_posts = Post.objects.select_related('author').order_by('-created_at')[:5]
    # 对每篇文章的内容进行Markdown处理
    for post in latest_posts:
        post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    return render(request, 'blog/home.html', {'latest_posts': latest_posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    return render(request, 'blog/post_detail.html', {'post': post})

def category(request, category_name):
    # 获取指定分类下的所有文章，并确保包含作者信息
    posts = Post.objects.filter(category=category_name).select_related('author').order_by('-created_at')
    # 对每篇文章的内容进行Markdown处理
    for post in posts:
        post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    return render(request, 'blog/category.html', {'category_name': category_name, 'posts': posts})

def tag(request, tag_name):
    # 获取指定标签下的所有文章，并确保包含作者信息
    posts = Post.objects.filter(tags__name=tag_name).select_related('author').order_by('-created_at')
    # 对每篇文章的内容进行Markdown处理
    for post in posts:
        post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    return render(request, 'blog/tag.html', {'tag_name': tag_name, 'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def search(request):
    query = request.GET.get('query')
    posts = []
    if query:
        # 搜索标题或内容包含查询词的文章，并确保包含作者信息
        posts = Post.objects.filter(title__icontains=query).select_related('author').order_by('-created_at')
        # 对每篇文章的内容进行Markdown处理
        for post in posts:
            post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    return render(request, 'blog/search.html', {'posts': posts, 'query': query or ''})

def archive(request):
    # 获取所有文章，按创建时间倒序排列
    posts = Post.objects.select_related('author').order_by('-created_at')
    # 对每篇文章的内容进行Markdown处理
    for post in posts:
        post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
    return render(request, 'blog/archive.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content, author=request.user, created_at=timezone.now())
            return redirect('post_list')
    return render(request, 'blog/create_post.html')

@login_required
def profile(request):
    # 检查是否有user_id参数
    user_id = request.GET.get('user_id')
    
    if user_id:
        # 查看其他用户的个人主页
        user = get_object_or_404(User, id=user_id)
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            # 如果用户没有个人资料，则创建一个
            profile = UserProfile.objects.create(user=user)
        
        # 获取该用户发布的所有博客
        user_posts = Post.objects.filter(author=user).order_by('-created_at')
        # 对每篇文章的内容进行Markdown处理
        for post in user_posts:
            post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
        
        # 不允许编辑其他用户的资料
        can_edit = False
    else:
        # 查看自己的个人主页
        user = request.user
        try:
            profile = user.userprofile
        except UserProfile.DoesNotExist:
            # 如果用户没有个人资料，则创建一个
            profile = UserProfile.objects.create(user=user)
        
        # 获取当前用户发布的所有博客
        user_posts = Post.objects.filter(author=user).order_by('-created_at')
        # 对每篇文章的内容进行Markdown处理
        for post in user_posts:
            post.content = markdown.markdown(post.content, extensions=['extra', 'codehilite'])
        
        can_edit = True
        
        if request.method == 'POST':
            # 更新用户信息
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            
            if email is not None:
                user.email = email
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.last_name = last_name
            user.save()
            
            # 更新用户资料
            bio = request.POST.get('bio')
            if bio is not None:
                profile.bio = bio
            profile.save()
            
            return redirect('profile')
    
    return render(request, 'blog/profile.html', {'profile': profile, 'user_posts': user_posts, 'can_edit': can_edit, 'view_user': user})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # 检查当前用户是否是文章作者
    if request.user != post.author:
        return HttpResponseForbidden("您没有权限编辑这篇文章")
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            post.title = title
            post.content = content
            post.save()
            messages.success(request, '文章更新成功！')
            return redirect('post_detail', post_id=post.id)
    
    return render(request, 'blog/edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # 检查当前用户是否是文章作者
    if request.user != post.author:
        return HttpResponseForbidden("您没有权限删除这篇文章")
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, '文章删除成功！')
        return redirect('post_list')
    
    return render(request, 'blog/delete_post.html', {'post': post})
