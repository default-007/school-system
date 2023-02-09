from django.db import models
from django.urls import reverse
from django.conf import settings
from authentication.models import User
from simple_history.models import HistoricalRecords
from home.models import *
from constants import *
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)",
    )
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


class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)",
    )
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


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, help_text="Enter Author or Publisher")
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book",
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    total_copies = models.IntegerField(
        blank=True,
        null=True,
    )
    available_copies = models.IntegerField(
        blank=True,
        null=True,
    )
    pic = models.ImageField(
        blank=True,
        null=True,
        upload_to="book_image",
        default="../static/paradox/images/img/coming.jpg",
    )
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

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    # __str__ method is used to override default string returnd by an object
    def __str__(self):
        return self.title

    def get_picture(self):
        no_picture = "../static/paradox/images/img/coming.jpg"
        try:
            return self.pic.url
        except:
            return no_picture


class Borrower(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
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
        return self.student.first_name + " borrowed " + self.book.title
