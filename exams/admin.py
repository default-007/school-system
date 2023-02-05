from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

# Register your models here.


class GradeAdmin(SimpleHistoryAdmin):
    list_display = ["student", "session", "term", "subject", "remark", "total"]


admin.site.register(Grade, GradeAdmin)
admin.site.register(GradeScale, SimpleHistoryAdmin)
admin.site.register(Ranking, SimpleHistoryAdmin)
