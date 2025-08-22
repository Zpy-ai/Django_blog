# ZPY博客项目 📘

> 一个基于Django开发的现代化个人博客系统，具有文章发布、分类管理、用户评论等功能。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square" alt="Python Version">
  <img src="https://img.shields.io/badge/Django-5.2.5-green?style=flat-square" alt="Django Version">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=flat-square" alt="License">
</p>

这是一个基于Django开发的个人博客系统，具有文章发布、分类管理、用户评论等功能。

## 🌟 功能特点

- 🔐 **用户认证和权限管理** - 完整的用户注册、登录和权限控制系统
- 📝 **文章发布和分类管理** - 支持文章创建、编辑和分类管理
- 💬 **评论系统** - 用户可以对文章进行评论和互动
- ⚙️ **管理员后台** - 提供便捷的后台管理界面
- 📱 **响应式设计** - 适配各种设备屏幕尺寸
- 📋 **Markdown语法支持** - 支持使用Markdown语法编写文章
- 🖋️ **可调整大小的文章编辑框** - 提供更大的编辑区域，支持垂直调整大小

## 🚀 快速开始

### 📦 环境准备

确保已安装Python 3.8+和pip包管理工具。

### 🛠️ 安装步骤

1. **克隆项目到本地**
   ```bash
   git clone <项目地址>
   ```

2. **进入项目目录**
   ```bash
   cd myblog
   ```

3. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

4. **数据库迁移**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **创建超级用户**
   ```bash
   python manage.py createsuperuser
   ```

6. **运行开发服务器**
   ```bash
   python manage.py runserver
   ```

> 🎉 安装完成后，访问 `http://127.0.0.1:8000` 查看博客网站

## 📁 项目结构

```
myblog/
├── blog/              # 博客应用
│   ├── templates/     # 博客模板
│   ├── static/        # 博客静态文件
│   └── views.py       # 博客视图逻辑
├── myblog/            # 项目配置
│   ├── settings.py    # 项目设置
│   └── urls.py        # URL路由配置
├── static/            # 全局静态文件
├── templates/         # 全局模板文件
├── manage.py          # Django管理脚本
└── requirements.txt   # 项目依赖
```

## 📋 Markdown支持

本项目支持Markdown语法，用户可以在文章编辑页面使用Markdown语法编写文章。主要特性包括：

- 🎯 **标题、列表、引用等基本语法** - 支持标准Markdown语法
- 💻 **代码块高亮显示** - 支持多种编程语言语法高亮
- 🔗 **链接和图片插入** - 轻松插入链接和图片

## 🖋️ 文章编辑框

文章创建和编辑页面的文本输入框经过优化，具有更大的编辑区域和可调整大小的功能，提升写作体验。

- 📏 **可调整大小** - 支持垂直拖拽调整编辑框高度
- 📐 **优化布局** - 提供更大的编辑区域，方便长文写作

## 🧰 技术栈

- 🐍 **Python 3.x** - 编程语言
- 🌐 **Django 5.2.5** - Web框架
- 🗄️ **SQLite** - 开发环境数据库
- 🎨 **HTML/CSS/JavaScript** - 前端技术

## 📄 许可证

本项目采用MIT许可证，详情请见[LICENSE](LICENSE)文件。

---

<p align="center">
  <strong>🎉 感谢使用ZPY博客项目！</strong>
</p>
