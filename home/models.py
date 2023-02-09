from django.db import models
from django.urls import reverse
from django.conf import settings
from authentication.models import User
from academics.models import Session
from constants import *
from academics.models import *
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.utils import timezone as tz


class Student(models.Model):
    name = models.CharField(max_length=55, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    in_class = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    fee_discount = models.IntegerField(default=0, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=6, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    year_of_admission = models.DateField(blank=True, null=True)
    roll_number = models.CharField(max_length=50, blank=True, null=True)
    lunch = models.BooleanField(default=True, null=True)
    active = models.BooleanField(default=True, null=True)
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

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"

    def __str__(self):
        return self.name + " " + self.roll_number


# Create your models here.


def get_terms():
    term = "First"
    now = tz.now()
    date = tz.localtime(now).date()
    setting = Setting.objects.first()

    if setting:
        st_begins, st_ends = setting.st_begins, setting.st_ends
        tt_begins, tt_ends = setting.tt_begins, setting.tt_ends
        if (st_begins and st_begins) and (date >= st_begins) and (date <= st_ends):
            term = "Second"
        if (tt_begins and tt_ends) and (date >= tt_begins) and (date <= tt_ends):
            term = "Third"
    return term


class Setting(models.Model):
    school_name = models.CharField(max_length=100)
    school_logo = models.ImageField(upload_to="pictures/", blank=True, null=True)
    school_address = models.CharField(max_length=300, blank=True, null=True)
    school_town = models.CharField(max_length=100, blank=True, null=True)
    school_slogan = models.CharField(max_length=200, blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    business_phone1 = models.CharField(max_length=11, blank=True, null=True)
    social_link1 = models.CharField(max_length=200, blank=True, null=True)
    ft_begins = models.DateField(blank=True, null=True)
    ft_ends = models.DateField(blank=True, null=True)
    st_begins = models.DateField(blank=True, null=True)
    st_ends = models.DateField(blank=True, null=True)
    tt_begins = models.DateField(blank=True, null=True)
    tt_ends = models.DateField(blank=True, null=True)
    history = HistoricalRecords()

    def get_logo(self):
        no_logo = settings.STATIC_ROOT + "/img/logo.png"
        try:
            return self.school_logo.url
        except:
            return no_logo

    def __str__(self):
        return self.school_name


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    unread = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


class Sms(models.Model):
    to_user = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    date_send = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=250)
    status = models.CharField(max_length=1, choices=STATUS, default=PENDING)
