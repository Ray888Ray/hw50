from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if last_name or first_name:
            pass
        else:
            raise forms.ValidationError('Fill out First name or Second name ')


# class MyUserCreationForm(forms.ModelForm):
#     password = forms.CharField(label="Password", strip=False, required=True, widget=forms.PasswordInput)
#     password_confirm = forms.CharField(label="Confirm password", required=True, widget=forms.PasswordInput
#     ,strip=False)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError('passwords are not the same!')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
