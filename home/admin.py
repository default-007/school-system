from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin

# from import_export import resources
# from import_export.admin import ImportMixin


class UserAdmin(SimpleHistoryAdmin):
    list_display = ["email", "last_name", "first_name"]

    search_fields = ["first_name", "last_name"]


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = [
            "roll_number",
            "name",
            "dob",
            "in_class",
            "address",
            "year_of_admission",
        ]


@admin.register(Student)
class StudentAdmin(ImportMixin, SimpleHistoryAdmin):
    list_display = [
        "roll_number",
        "name",
        "dob",
        "address",
        "year_of_admission",
        "changed_by",
    ]
    history_list_display = ["status"]
    resource_class = StudentResource


admin.site.register(User, UserAdmin)

admin.site.register(Notification, SimpleHistoryAdmin)

admin.site.register(Setting, SimpleHistoryAdmin)

admin.site.register(Sms, SimpleHistoryAdmin)
