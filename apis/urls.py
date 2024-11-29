"""
URL configuration for apis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_app.views import login, register, home, view_content, logout, my_blogs, create_blog,delete_blog, edit_blog, mod_blogs, only_admin, change

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('home', home, name="home"),
    path('blog/<int:id>', view_content, name="view_blog"),
    path("logout", logout, name="logout"),
    path("home/myblogs", my_blogs, name="my_blogs"),
    path("home/myblogs/create", create_blog, name="create_blog"),
    path("home/myblogs/delete/<int:id>", delete_blog, name="delete_blog"),
    path("home/myblogs/edit/<int:id>", edit_blog, name="edit_blog"),
    path("home/modblogs", mod_blogs, name="mod_blogs"),
    path("home/admin", only_admin, name="admin"),
    path("change/<int:id>", change, name="change"),
    
]
