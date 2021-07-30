from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from . import models
from django.http import Http404


def login_required_decorator(func):
    return login_required(func, login_url='login-page')


def check_users_priorities(types):
    def inner(func):
        def wrapper(*args, **kwargs):
            if args[0].user.user_type in types:
                return func(*args, *kwargs)
            else:
                raise Http404
        return wrapper
    return inner


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login-page')


def index_page(request):
    users = models.User.objects.all()
    ctx = {
        'users': users
    }
    return render(request, 'index.html', ctx)


@login_required_decorator
@check_users_priorities([1])
def user_create(request):
    if request.POST:
        user = models.User.objects.create_user(
            full_name=request.POST.get('full-name'),
            email=request.POST.get('email'),
            password=request.POST.get('password'),
            user_type=request.POST.get('user_type')
        )

    return render(request, 'form.html')


def login_page(request):
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    user = (authenticate(email=email, password=password))
    if user is not None:
        login(request, user)
        return redirect('home-page')

    return render(request, 'login.html')


def register_page(request):
    if request.POST:
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = models.User.objects.create_user(full_name=full_name, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home-page')
    return render(request, 'register.html')