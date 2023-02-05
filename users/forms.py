from django import forms
from .models import *


class AddParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        exclude = ("parent",)


class ProfilePictureForm(forms.Form):
    picture = forms.ImageField()


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )


class EmailForm(forms.Form):
    email = forms.EmailField()


class UpdateProfileForm(forms.Form):
    email = forms.EmailField(label="Email Address", required=False)
    phone = forms.CharField(
        max_length=10, min_length=10, label="Phone number", required=False
    )
    firstname = forms.CharField(max_length=30, label="Firstname", required=False)
    surname = forms.CharField(max_length=30, label="Firstname", required=False)
    address = forms.CharField(max_length=120, label="Address", required=False)
    othername = forms.CharField(max_length=50, label="Othername", required=False)
