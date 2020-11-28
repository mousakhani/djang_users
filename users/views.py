from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

# Create your views here.
from users.forms import CustomUserForm
from users.models import CustomUser


def signup(request):
    if request.POST:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('home')
        else:
            errors = (
                form.errors.get('username') or '',
                form.errors.get('password2'),
            )
            return render(request, 'registration/signup.html', {'errors': errors})
    else:
        return render(request, 'registration/signup.html', {})


def login(request):
    error = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error = 'نام کاربری و گذرواژه هم خواند ندارد'
    return render(request, 'registration/login.html', {'errors': error})


def password_recovery(request):
    if request.GET.get('email'):
        email = request.GET.get('email')
        return redirect('users:password_recovery')
    return  render(request, 'registration/password_recovery.html', {})
