from django.shortcuts import render, redirect, HttpResponse
from api_app.forms import Login_form, Register_form, Create_Blog, Edit_Blog, Admin_Page
from django.http import JsonResponse
from api_app.models import App_User, Blogs
import jwt
import bcrypt
from jwt.exceptions import ExpiredSignatureError
from datetime import date
from time import time
from apis.settings import SECRET_KEY, ALGORITHM, EXPIRY_MINUTES
# Create your views here.


def Validator(func):
    def wrapper(request, *args, **kwargs):
        try:
            token = request.COOKIES.get("AccessToken")
            decoded = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
            request.decoded = decoded
            return func(request, *args, **kwargs)
        except ExpiredSignatureError:
            return render(request, "Error_page.html", {
                "error": {
                    "code": "401",
                    "message": "JWT signature expired. Please login again."
                }
            })
    return wrapper


def login(request):
    form = Login_form()
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            try:
                data = App_User.objects.get(username=user)
                password = bytes(passw, encoding="utf-8")
                hashed = bytes(data.password[2:-1], encoding="utf-8")
                res = bcrypt.checkpw(password, hashed)
                if res:
                    user_data = {"role": data.role,
                                 "username": data.username,
                                 "exp": time() + (EXPIRY_MINUTES * 60)}
                    access_token = jwt.encode(
                        user_data, key=SECRET_KEY, algorithm=ALGORITHM)

                    response = redirect("home")
                    response.set_cookie(
                        "AccessToken", access_token)
                    return response
                else:
                    return render(request, "Error_page.html", {
                "error": {
                    "code": "401",
                    "message": "Invalid Password !"
                }
            })
            except App_User.DoesNotExist:
                return render(request, "Error_page.html", {
                "error": {
                    "code": "404",
                    "message": "User Not Found "
                }
            })
    return render(request, "login.html", {"form": form})


def register(request):
    form = Register_form()
    code = 100
    if request.method == "POST":
        form = Register_form(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            byte = password.encode("utf-8")
            salt = bcrypt.gensalt()
            hashed_pass = bcrypt.hashpw(byte, salt)
            try:
                App_User.objects.get(username=username)
                code = 401
            except:
                App_User.objects.create(
                    username=username, password=hashed_pass)
                code = 201
    return render(request, "register.html", {"form": form, "code": code})


def home(request):
    auth = False
    if request.COOKIES.get("AccessToken"):
        auth = True
    data = Blogs.objects.all()
    blog_data = []
    for i in data:
        blog_data.append({'blog_title': i.blog_title,
                         "blog_id": i.blog_id, "blog_date": i.blog_date})
    response = render(request, "Home.html", {
                      "data": blog_data, "is_authenticated": auth})
    return response


def view_content(request, id):
    data = Blogs.objects.get(blog_id=id)
    blog_data = {"data_title": data.blog_title,
                 "data_content": data.blog_content,
                 "data_date": data.blog_date}
    return render(request, "View.html", {"data": blog_data})


def logout(request):
    response = redirect("home")
    response.delete_cookie('AccessToken')
    response.delete_cookie('section')
    return response


@Validator
def my_blogs(request):
    decoded = request.decoded
    username = decoded['username']
    data = Blogs.objects.filter(user=username)
    formatted_data = []
    if len(data) != 0:
        for i in data:
            formatted_data.append(
                {"blog_title": i.blog_title, "blog_date": i.blog_date, "blog_id": i.blog_id})
    if len(formatted_data) != 0:
        data_value = True
    else:
        data_value = False
    return render(request, "my_blogs.html", {"data": formatted_data, "data_value": data_value})


@Validator
def mod_blogs(request):
    decoded = request.decoded
    role = decoded['role']
    if role == "mod" or role == "admin":
        data = Blogs.objects.all()
        formatted_data = []
        if len(data) != 0:
            for i in data:
                formatted_data.append(
                    {"blog_title": i.blog_title, "blog_date": i.blog_date, "blog_id": i.blog_id})
        if len(formatted_data) == 0:
            data_value = False
        else:
            data_value = True
        return render(request, "Mod_blog.html", {"data": formatted_data, "data_value": data_value})
    else:
        return render(request, "Error_page.html", {
                "error": {
                    "code": "403",
                    "message": "Dont Have Access to this Page !"
                }
            })


@Validator
def create_blog(request):
    form = Create_Blog()
    if request.method == "POST":
        form = Create_Blog(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            f_date = date.today().strftime("%b %d, %Y")
            decoded = request.decoded
            username = decoded['username']
            Blogs.objects.create(
                blog_date=f_date, blog_title=title, blog_content=content, user=username)
            return redirect("my_blogs")
    return render(request, "Create_blog.html", {"form": form})


@Validator
def delete_blog(request, id):
    decoded = request.decoded
    blog = Blogs.objects.get(blog_id=id)
    if decoded['role'] in ['admin', 'mod'] or decoded['username'] == blog.user:
        try:
            blog.delete()
            return redirect("home")
        except:
            return render(request, "Error_page.html", {
                "error": {
                    "code": "404",
                    "message": "Blog Doesnot Exist !"
                }
            })
    else:
        return render(request, "Error_page.html", {
                "error": {
                    "code": "403",
                    "message": "Can't Delete the Blog !"
                }
            })


@Validator
def only_admin(request):
    decoded: dict = request.decoded
    section = request.COOKIES.get("section")
    data = App_User.objects.all()
    form = Admin_Page()
    userlogged_in = decoded['username']
    role = decoded['role']
    if role == "admin":
        formatted_data = []
        if "section" in request.COOKIES:
            if section == "users":
                for i in data:
                    formatted_data.append(
                        {"username": i.username, "user_id": i.user_id, "user_role": i.role})
                new_data = [
                    entry for entry in formatted_data if entry['username'] != userlogged_in]
            elif section == "blogs":
                data = Blogs.objects.all()
                formatted_data = []
                if len(data) != 0:
                    for i in data:
                        formatted_data.append(
                            {"blog_title": i.blog_title, "blog_date": i.blog_date, "blog_id": i.blog_id})
                new_data = formatted_data
            if len(new_data) == 0:
                data_value = False
            else:
                data_value = True
            return render(request, "Admin_page.html", {"section": section, "data": new_data, "form": form, "data_value": data_value})
        return render(request, "Admin_page.html")
    else:
        return render(request, "Error_page.html", {
                "error": {
                    "code": "403",
                    "message": "Don't Have Access to this Page !"
                }
            })


@Validator
def edit_blog(request, id):
    form = Edit_Blog()
    blog = Blogs.objects.get(blog_id=id)
    obj = {"blog_title": blog.blog_title, "blog_content": blog.blog_content}
    if request.method == "POST":
        form = Edit_Blog(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            decoded = request.decoded
            if decoded['username'] == blog.user:
                blog.blog_title = title
                blog.blog_content = content
                blog.save()
                return redirect("my_blogs")
    form.custom(obj)
    date = blog.blog_date
    return render(request, "Edit_Blog.html", {"form": form, "date": date})


def change(request, id):
    user_data = App_User.objects.get(user_id=id)
    if request.method == "POST":
        form = Admin_Page(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            user_data.role = role
            user_data.save()
    return redirect("admin")
