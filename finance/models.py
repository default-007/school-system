from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from authentication.models import User
from constants import *
from academics.models import *
from dashboard.models import *
from django.utils.translation import gettext_lazy as _


class OtherFeeCharges(models.Model):
    name = models.CharField(max_length=100)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )
    amount = models.IntegerField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(choices=TERM, max_length=7)
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


""" class PayType(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    for_fee = models.ForeignKey(FeeType, on_delete=models.CASCADE, blank=True)
    paid_amount = models.IntegerField(null=True, blank=True)
    due_amount = models.IntegerField(blank=True, null=True)
    date_paid = models.DateField(auto_now_add=True)
    overdraft = models.IntegerField(null=True, blank=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=100)
    payment_status = models.CharField(
        choices=PAYMENT_STATUS, blank=True, max_length=100
    )
    receipt_number = models.CharField(max_length=100, blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(choices=TERM, max_length=7)
    ctext = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.student.roll_number
 """


class Fee(models.Model):
    for_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    term = models.CharField(choices=TERM, max_length=50, blank=True, null=True)
    tuition = models.IntegerField(null=True, blank=True)
    lunch = models.IntegerField(null=True, blank=True)
    activity = models.IntegerField(null=True, blank=True)
    maintenance = models.IntegerField(null=True, blank=True)
    examination = models.IntegerField(null=True, blank=True)
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
        return self.for_class.name + " " + self.term + " " + str(self.total_amount)

    @property
    def total_amount(self):
        amount = (
            int(self.tuition)
            + int(self.lunch)
            + int(self.activity)
            + int(self.maintenance)
            + int(self.examination)
        )
        return amount


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    paid_amount = models.IntegerField()
    due_amount = models.IntegerField(blank=True, null=True)
    date_paid = models.DateTimeField(auto_now_add=True)
    overdraft = models.IntegerField(default=0)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50)
    payment_status = models.CharField(
        choices=PAYMENT_STATUS, max_length=50, blank=True, null=True
    )
    term = models.CharField(choices=TERM, max_length=7)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=100, blank=True, null=True)
    ctext = models.CharField(max_length=100, blank=True, null=True)
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
        return self.student.roll_number + " " + self.paid_amount


class Expense(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, default=Session.get_current_session()
    )
    term = models.CharField(choices=TERM, max_length=7, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
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
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("expense_detail", kwargs={"pk": self.pk})
