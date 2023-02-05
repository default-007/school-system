from django.db import models
from django.urls import reverse
from django.conf import settings
from authentication.models import User
from simple_history.models import HistoricalRecords
from constants import *
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Session(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=200, blank=True, null=True)
    current_session = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def get_current_session():
        try:
            return Session.objects.get(current_session=True).id
        except:
            pass

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100, unique=True)
    note = models.CharField(max_length=200, blank=True, null=True)
    changed_by = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, blank=True, null=True
    )
    history = HistoricalRecords(user_model=User)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
    changed_by = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, blank=True, null=True
    )
    history = HistoricalRecords(user_model=User)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    changed_by = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, blank=True, null=True
    )
    history = HistoricalRecords(user_model=User)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "classes"


def get_current_session():
    return Session.objects.get(current_session=True).id


class SubjectAssign(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(choices=TERM, max_length=7)
    clss = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, blank=True)


class SectionAssign(models.Model):
    section_head = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    placeholder = models.CharField(max_length=100)


class Setting(models.Model):
    school_name = models.CharField(max_length=100)
    school_logo = models.ImageField(upload_to="pictures/", blank=True, null=True)
    school_address = models.CharField(max_length=300, blank=True, null=True)
    school_town = models.CharField(max_length=100, blank=True, null=True)
    school_slogan = models.CharField(max_length=200, blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    business_phone1 = models.CharField(max_length=11, blank=True, null=True)
    social_link1 = models.CharField(max_length=200, blank=True, null=True)
    changed_by = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, blank=True, null=True
    )
    history = HistoricalRecords(user_model=User)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def get_logo(self):
        no_logo = settings.STATIC_ROOT + "/img/logo.png"
        try:
            return self.school_logo.url
        except:
            return no_logo

    def __str__(self):
        return self.school_name
