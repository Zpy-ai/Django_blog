# Register your models here.
from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Post, UserProfile

class MyAdminSite(AdminSite):
    site_header = 'ZPY博客管理后台'  # 设置管理后台标题
    site_title = 'ZPY博客管理'
    index_title = '欢迎来到ZPY博客管理后台'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)
        
    def each_context(self, request):
        context = super().each_context(request)
        context['site_header'] = self.site_header
        context['site_title'] = self.site_title
        context['index_title'] = self.index_title
        return context
    
    def get_urls(self):
        from django.urls import path
        from django.views.generic import RedirectView
        urls = super().get_urls()
        # 添加自定义CSS
        urls += [
            path('admin/css/admin.css', RedirectView.as_view(url='/static/css/admin.css', permanent=True)),
        ]
        return urls

# 创建自定义admin站点实例
admin_site = MyAdminSite(name='myadmin')

# 注册模型到自定义admin站点
admin_site.register(Post)
admin_site.register(UserProfile)

# 为了保持Django默认的admin站点也可用，也注册到默认站点
admin.site.register(Post)
admin.site.register(UserProfile)