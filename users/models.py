from django.db import models
from authentication.models import User
from simple_history.models import HistoricalRecords
from dashboard.models import Student


# Create your models here.
class Parent(models.Model):
    parent = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="parent_user"
    )
    student = models.ManyToManyField(Student, related_name="guardians")
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
        return str(self.parent.get_full_name())


class Teacher(models.Model):
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teacher_user"
    )
    tac_no = models.CharField(max_length=10, unique=True, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
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
        return self.teacher.get_full_name()
