from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import signup, password_recovery, login

app_name = 'users'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('password/recovery/', password_recovery, name='password_recovery'),
]
