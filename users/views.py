import random
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template
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
        email_user = request.GET['email']
        user = CustomUser.objects.filter(email__exact=email_user)
        if user.count() != 0:  # mail not exist
            password = password_generator()
            username = user.get().username
            user = CustomUser.objects.get(username=username)
            user.set_password(password)
            user.save()

            # مقادیر ارسالی مانند رمز عبور جدید و... را در قالب template قرار می دهد.
            rendered_message = get_template('emails/email_recovery_message.html').render({
                'password': password, 'username': user.get().first_name
            })
            # fail_silently=True
            # پیش فرض False
            # اگر مقدار این False باشد، خطاهایی که هنگام ارسال ایمیل می تواند رخ دهد را نشان می دهد.
            # smtplib.SMTPException
            #
            # hmlt_message
            # اگر متن پیام از طریق این ارسال شود، به صورت یک سند html فرض شده، و تگهای html و کدهای css در ایمیل اجرا خواهند شد
            # اگر از طریق این ارسال نشود، تگها و کدها خود جزوی از متن پیام اسلی تلقی می شود.
            send_mail(subject='بازیابی رمز عبور', message='', from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[email_user, ],
                      fail_silently=True,
                      html_message=rendered_message)
            # نوع فایل متنی را مشخص می کند. در صورتی که مقدار html قرار داده نشود، متن ارسالی حاوی تگ های html نیز خواهد بود.
            # توجه شود که کدهای css باید به صورت inline نوشته شود.
            return render(request, 'registration/password_recovery.html', {'errors': 'رمز عبور جدید برای شما ارسال شد'})
        else:
            return render(request, 'registration/password_recovery.html', {'errors': 'ایمیل وارد شده ثبت نشده است'})
    else:
        return render(request, 'registration/password_recovery.html', {})
