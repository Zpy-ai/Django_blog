from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('archive/', views.archive, name='archive'),
    path('login/', __import__('blog.auth_views').auth_views.login_view, name='login'),
    path('register/', __import__('blog.auth_views').auth_views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('create/', views.create_post, name='create_post'),
    path('profile/', views.profile, name='profile'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]