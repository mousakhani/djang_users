from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phone',)

    # def clean_password2(self):
    #     super(CustomUserForm, self).clean_password()
    #     pass1 = self.cleaned_data['password1']
    #     pass2 = self.cleaned_data['password2']
    #     if (pass1 is None) or (pass2 is None):
    #         return 'فیلدهای گذرواژه باید پر شود'
    #     if pass1 != pass2:
    #         return 'گذرواژه با تکرار آن هم خوانی ندارد'
    #     return pass1

    # def clean(self):
    #     super(CustomUserForm, self).clean()
    #     if self._errors.as_data().get('password2'):
    #         self._errors = self.error_class(['خطا در گذرواژه رخ داده است'])
    #     if self._errors.error_class.['username']:
    #         self._errors = self.error_class(['خطای نام کاربری رخ داده است'])
    #     # if len(self.cleaned_data.get('username')):
    #     #     self._errors['username'] = self.error_class(['نام کاربری خیلی کوتاه است'])
    #
    #     return self.cleaned_data

    #
    # username = forms.CharField(max_length=50)
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    # email = forms.EmailField(max_length=100)
    # phone = forms.CharField(max_length=11)
    # location = forms.CharField(max_length=100)
    # bio = forms.Textarea()
