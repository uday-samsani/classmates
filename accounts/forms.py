from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth import get_user_model

from .models import stream_choice, gender_choice, course_choice


class AccountChangeForm(UserCreationForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',
                  'username', 'dob', 'gender', 'password')


class AccountCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name', widget=forms.TextInput(attrs={'placeholder': 'Jon'}))
    last_name = forms.CharField(
        label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Doe'}))
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={'placeholder': 'JonDoe@mail.com'}))
    phn_num = forms.CharField(
        label='Phone Number', widget=forms.TextInput(attrs={'placeholder': '9999999999'}))
    reg_num = forms.CharField(
        label='Registration Number', widget=forms.TextInput(attrs={'placeholder': '14PA1A1111'}))
    dob = forms.CharField(
        label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.CharField(
        label='Gender', widget=forms.Select(choices=gender_choice))
    stream = forms.CharField(
        label='Stream', widget=forms.Select(choices=stream_choice))
    course = forms.CharField(
        label='Course', widget=forms.Select(choices=course_choice))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username',
                  'gender', 'dob', 'phn_num',
                  'reg_num', 'stream', 'course',
                  'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(AccountCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.dob = self.cleaned_data['dob']
        user.phn_num = self.cleaned_data['phn_num']
        user.reg_num = self.cleaned_data['reg_num']
        user.stream = self.cleaned_data['stream']
        user.course = self.cleaned_data['course']
        user.gender = self.cleaned_data['gender']
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()

        return user
