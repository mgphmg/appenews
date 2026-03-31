from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User , Article
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'enews/home.html')

def login_options(request):
    return render(request, 'enews/welcome.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            #  FIXED ROLE CHECK
            if user.role == 'admin' or user.is_superuser:
                return redirect('admin_home')

            elif user.role == 'editor':
                return redirect('editor_home')

            elif user.role == 'reporter':
                return redirect('reporter_home')

            else:
                return redirect('user_home')

        else:
            return render(request, "enews/login.html", {"error": "Invalid credentials"})

    return render(request, "enews/login.html")


def register(request):
    if request.method == "POST":
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        username=email
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fullname
        )

        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'enews/register.html')

@login_required
def user_home(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'enews/user_home.html',{ 'articles': articles})


def admin_home(request):
    return render(request, 'enews/dashboard.html')

def editor_home(request):
    return render(request, 'enews/editor_home.html')

def reporter_home(request):
    return render(request, 'enews/reporter_home.html')


def user_logout(request):
    logout(request)  # destroys session
    return redirect('login')  # redirect to login page

def admin_article(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        Article.objects.create(
            title=title,
            description=description,
            image=image,
            author=request.user
        )
        return render(request, 'enews/article_creation.html',{'message':'Article Saved'})
    return render(request, 'enews/article_creation.html')