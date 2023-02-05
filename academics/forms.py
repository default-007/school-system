from django import forms
from .models import *
from authentication.models import User
from constants import *


class SubjectForm(forms.ModelForm):
    name = forms.CharField(
        label="Subject name",
        widget=forms.TextInput(attrs={"class": "form-control subject"}),
    )

    class Meta:
        model = Subject
        fields = [
            "name",
        ]


class SessionForm(forms.ModelForm):
    name = forms.CharField(
        label="Session name",
        widget=forms.TextInput(attrs={"class": "form-control session"}),
    )
    note = forms.CharField(
        label="Session note",
        widget=forms.TextInput(attrs={"class": "form-control session"}),
    )
    current_session = forms.BooleanField(
        label="Current session",
        widget=forms.NullBooleanSelect(attrs={"class": "form-control session"}),
    )

    class Meta:
        model = Session
        fields = [
            "name",
            "note",
            "current_session",
        ]


class SectionForm(forms.ModelForm):
    name = forms.CharField(
        label="Section name",
        widget=forms.TextInput(attrs={"class": "form-control section"}),
    )
    note = forms.CharField(
        label="Section note",
        widget=forms.TextInput(attrs={"class": "form-control section"}),
    )

    class Meta:
        model = Section
        fields = [
            "name",
            "note",
        ]


class ClassForm(forms.ModelForm):
    name = forms.CharField(
        label="Class name",
        widget=forms.TextInput(attrs={"class": "form-control section"}),
    )
    section = forms.ModelChoiceField(
        label="Class note",
        queryset=Section.objects.all(),
        widget=forms.RadioSelect(attrs={"class": "section"}),
    )
    subjects = forms.ModelMultipleChoiceField(
        label="Class subjects",
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "section"}),
    )

    class Meta:
        model = Class
        fields = [
            "name",
            "section",
            "subjects",
        ]


class SubjectAssignForm(forms.ModelForm):
    session = forms.ModelChoiceField(
        label="Session",
        queryset=Session.objects.all(),
        widget=forms.Select(attrs={"class": "form-control section"}),
    )
    term = forms.ChoiceField(
        label="Term", choices=TERM, widget=forms.RadioSelect(attrs={"class": "subject"})
    )
    clss = forms.ModelChoiceField(
        label="Class",
        queryset=Class.objects.all(),
    )
    teacher = forms.ModelChoiceField(
        label="Teacher", queryset=User.objects.filter(is_teacher=True)
    )
    subjects = forms.ModelMultipleChoiceField(
        label="Subjects",
        queryset=Subject.objects.all(),
    )

    class Meta:
        model = SubjectAssign
        fields = ["clss", "teacher", "subjects", "term", "session"]


class SectionAssignForm(forms.ModelForm):
    section_head = forms.ModelChoiceField(
        label="Section Head", queryset=User.objects.filter(is_teacher=True)
    )
    section = forms.ModelChoiceField(label="Section", queryset=Section.objects.all())
    placeholder = forms.CharField(
        label="Placeholder", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = SectionAssign
        fields = ["section", "section_head", "placeholder"]
