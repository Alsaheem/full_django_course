from django import forms
from django.contrib.auth.models import User
from basic_app.models import userprofileinfo

class userForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class userprofileinfoform(forms.ModelForm):

    class Meta():
        model = userprofileinfo
        fields = ('portfolio_link','profile_pic')
