from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter your email again ')
    text = forms.CharField(widget=forms.Textarea)

# to make your own custom validator applies to all the field below....you use

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("make sure that the email fields match")


########################################      coment below    ######################################################3

# to make your own custom validators , like if you want the first name to start with z as a requirement
#and you check the documentation and didnt seee any thing about that particulr feature
# def check_for_z(value): #the vaue keyword tells django that its a validators
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("name needs to start with a Z")
#
#
#
#
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher =forms.CharField(required=False,
#                                  widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])
