# ZPY博客项目

这是一个基于Django开发的个人博客系统，具有文章发布、分类管理、用户评论等功能。

## 功能特点

- 用户认证和权限管理
- 文章发布和分类管理
- 评论系统
- 管理员后台
- 响应式设计
- Markdown语法支持
- 可调整大小的文章编辑框

## 安装步骤

1. 克隆项目到本地：
   ```
   git clone <项目地址>
   ```

2. 进入项目目录：
   ```
   cd myblog
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

4. 数据库迁移：
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. 创建超级用户：
   ```
   python manage.py createsuperuser
   ```

6. 运行开发服务器：
   ```
   python manage.py runserver
   ```

## 项目结构

```
myblog/
├── blog/              # 博客应用
├── myblog/            # 项目配置
├── static/            # 静态文件
├── templates/         # 模板文件
├── manage.py          # Django管理脚本
└── requirements.txt   # 项目依赖
```

## Markdown支持

本项目支持Markdown语法，用户可以在文章编辑页面使用Markdown语法编写文章。主要特性包括：

- 标题、列表、引用等基本语法
- 代码块高亮显示
- 链接和图片插入

## 文章编辑框

文章创建和编辑页面的文本输入框经过优化，具有更大的编辑区域和可调整大小的功能，提升写作体验。

## 技术栈

- Python 3.x
- Django 5.2.5
- SQLite (默认数据库)
- HTML/CSS/JavaScript

## 许可证

本项目仅供学习交流使用。
