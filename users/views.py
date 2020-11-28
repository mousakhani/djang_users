from django.contrib.auth import authenticate, login
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
            login(request, user)
            return redirect('home')
        else:
            errors = (
                form.errors.get('username') or '',
                form.errors.get('password2'),
            )
            return render(request, 'registration/signup.html', {'errors': errors})
    else:
        return render(request, 'registration/signup.html', {})
