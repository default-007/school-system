from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

# Register your models here.

admin.site.register(Parent, SimpleHistoryAdmin)
admin.site.register(Teacher, SimpleHistoryAdmin)
