from django import forms
from django.forms import ModelForm
from .models import *


class AddGenreForm(forms.ModelForm):
    name = forms.CharField(
        label="Genre Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Genre
        fields = [
            "name",
        ]


class AddLanguageForm(forms.ModelForm):
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Language
        fields = [
            "name",
        ]


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = [
            "changed_by",
        ]


class AddBorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        exclude = [
            "changed_by",
        ]
