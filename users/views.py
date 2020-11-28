import random

from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from djang_users import settings
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


def password_generator():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    length = random.randrange(8, 12)
    passowrd = ''
    for p in range(length):
        passowrd += random.choice(s)
    return passowrd


def password_recovery(request):
    if request.GET.get('email'):
        email = request.GET['email']
        user = CustomUser.objects.filter(email__exact=email)
        if user.count() != 0:  # mail not exist
            password = password_generator()
            username = user.get().username
            subject = 'بازیابی رمز عبور'
            msg = password
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, msg, from_email=from_email, recipient_list=[email, ])
            user = CustomUser.objects.get(username=username)
            user.set_password(password)
            user.save()
            return render(request, 'registration/password_recovery.html', {'errors': 'رمز عبور جدید برای شما ارسال شد'})
        else:
            return render(request, 'registration/password_recovery.html', {'errors': 'ایمیل وارد شده ثبت نشده است'})
    else:
        return render(request, 'registration/password_recovery.html', {})
