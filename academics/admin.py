from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

# from import_export import resources
# from import_export.admin import ImportMixin

# Register your models here.
admin.site.register(Session, SimpleHistoryAdmin)
admin.site.register(Section, SimpleHistoryAdmin)
admin.site.register(Subject, SimpleHistoryAdmin)
admin.site.register(Class, SimpleHistoryAdmin)
admin.site.register(SubjectAssign, SimpleHistoryAdmin)
