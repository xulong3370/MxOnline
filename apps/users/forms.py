# coding=utf-8


__author__ = '徐龙'
__date__ = '2017/6/9 19:49'
from django import forms
from captcha.fields import CaptchaField
from users.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ModifyPwdForms(forms.Form):
    password1 = forms.CharField(required=True,min_length=6)
    password2 = forms.CharField(required=True,min_length=6)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nick_name",'gender','birthday','address','mobile']