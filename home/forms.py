from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from authentication.models import User


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "gender",
        )


class StudentForm(forms.ModelForm):
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control student"})
    )
    roll_number = forms.CharField(
        label="Admission Number",
        widget=forms.TextInput(attrs={"class": "form-control student"}),
    )
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(
            attrs={
                "class": "form-control datepicker_input student",
                "placeholder": "yyyy-mm-dd",
            }
        ),
    )
    in_class = forms.ModelChoiceField(label="Class", queryset=Class.objects.all())
    gender = forms.ChoiceField(
        choices=GENDER,
        label="Gender",
        widget=forms.RadioSelect(attrs={"class": "student"}),
    )
    fee_discount = forms.DecimalField(
        label="Issued Fee Discount",
        max_digits=10,
        decimal_places=2,
        widget=forms.TextInput(
            attrs={"class": "form-control student", "placeholder": "..."}
        ),
    )
    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(
            attrs={"class": "form-control student", "placeholder": "Hospital Road"}
        ),
    )
    year_of_admission = forms.DateField(
        label="Year of Admission",
        widget=forms.DateInput(
            attrs={
                "class": "form-control datepicker_input student",
                "placeholder": "yyyy-mm-dd",
            }
        ),
    )

    class Meta:
        model = Student
        fields = [
            "name",
            "roll_number",
            "dob",
            "gender",
            "fee_discount",
            "address",
            "year_of_admission",
        ]


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
