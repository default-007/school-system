from django.db import models
from simple_history.models import HistoricalRecords
from constants import *
from academics.models import *


# Create your models here.
class Grade(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(choices=TERM, max_length=7)
    student = models.ForeignKey("dashboard.Student", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    fca = models.IntegerField(null=True, blank=True)
    sca = models.IntegerField(null=True, blank=True)
    exam = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(blank=True, null=True)
    grade = models.CharField(choices=GRADE, max_length=1, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
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
        return self.student.first_name + " " + self.term + " " + self.subject.name

    def compute_position(self, term):
        cs = Session.objects.get(current_session=True)
        total = 0
        all_score = Grade.objects.filter(student__id=self.student.id)
        for i in all_score:
            if i.total == None:
                total += 0
            else:
                total += float(i.total)
        try:
            r = Ranking.objects.get(session=cs, term=term, student=self.student)
            r.cumulative = total
            r.save()
        except Ranking.DoesNotExist:
            a = Ranking.objects.create(
                session=cs,
                term=term,
                student=self.student,
                cumulative=total,
            )


class GradeScale(models.Model):
    grade = models.CharField(choices=GRADE, max_length=100, unique=True)
    mark_from = models.IntegerField(unique=True)
    mark_upto = models.IntegerField(unique=True)
    remark = models.CharField(max_length=20, unique=True)
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


class Ranking(models.Model):
    student = models.ForeignKey("dashboard.Student", on_delete=models.CASCADE)
    term = models.CharField(max_length=12, choices=TERM)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    cumulative = models.FloatField()
    rank = models.CharField(max_length=5, blank=True, null=True)
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
