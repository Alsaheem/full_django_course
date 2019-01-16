from django import forms
from second_app.models import user
from django.core import validators


class NewUserForm(forms.ModelForm):

    class Meta():
        model = user
        fields = '__all__'
