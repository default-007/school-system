# Generated by Django 4.1.6 on 2023-02-09 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("academics", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Setting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("school_name", models.CharField(max_length=100)),
                (
                    "school_logo",
                    models.ImageField(blank=True, null=True, upload_to="pictures/"),
                ),
                (
                    "school_address",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "school_town",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "school_slogan",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "business_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "business_phone1",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                (
                    "social_link1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("ft_begins", models.DateField(blank=True, null=True)),
                ("ft_ends", models.DateField(blank=True, null=True)),
                ("st_begins", models.DateField(blank=True, null=True)),
                ("st_ends", models.DateField(blank=True, null=True)),
                ("tt_begins", models.DateField(blank=True, null=True)),
                ("tt_ends", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sms",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("to_user", models.CharField(max_length=10)),
                ("title", models.CharField(max_length=100)),
                ("date_send", models.DateTimeField(auto_now_add=True)),
                ("body", models.CharField(max_length=250)),
                (
                    "status",
                    models.CharField(
                        choices=[("D", "Draft"), ("S", "Delivered"), ("P", "Pending")],
                        default="P",
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=55, null=True)),
                ("dob", models.DateField(blank=True, null=True)),
                ("fee_discount", models.IntegerField(default=0, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("year_of_admission", models.DateField(blank=True, null=True)),
                ("roll_number", models.CharField(blank=True, max_length=50, null=True)),
                ("lunch", models.BooleanField(default=True, null=True)),
                ("active", models.BooleanField(default=True, null=True)),
                (
                    "changed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "in_class",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academics.class",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="academics.session",
                    ),
                ),
            ],
            options={
                "verbose_name": "student",
                "verbose_name_plural": "students",
            },
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("body", models.CharField(max_length=300)),
                ("unread", models.BooleanField(default=False)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalStudent",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=55, null=True)),
                ("dob", models.DateField(blank=True, null=True)),
                ("fee_discount", models.IntegerField(default=0, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=6,
                        null=True,
                    ),
                ),
                ("year_of_admission", models.DateField(blank=True, null=True)),
                ("roll_number", models.CharField(blank=True, max_length=50, null=True)),
                ("lunch", models.BooleanField(default=True, null=True)),
                ("active", models.BooleanField(default=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "changed_by",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "in_class",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="academics.class",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="academics.session",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical student",
                "verbose_name_plural": "historical students",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalSetting",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("school_name", models.CharField(max_length=100)),
                (
                    "school_logo",
                    models.TextField(blank=True, max_length=100, null=True),
                ),
                (
                    "school_address",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "school_town",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "school_slogan",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "business_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "business_phone1",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                (
                    "social_link1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("ft_begins", models.DateField(blank=True, null=True)),
                ("ft_ends", models.DateField(blank=True, null=True)),
                ("st_begins", models.DateField(blank=True, null=True)),
                ("st_ends", models.DateField(blank=True, null=True)),
                ("tt_begins", models.DateField(blank=True, null=True)),
                ("tt_ends", models.DateField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical setting",
                "verbose_name_plural": "historical settings",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
