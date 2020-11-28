from django.contrib import admin

# Register your models here.
from users.models import CustomUser


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = ['username','first_name','last_name','phone','email']