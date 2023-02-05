from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *


# Register your models here.
admin.site.register(Book, SimpleHistoryAdmin)
admin.site.register(Genre, SimpleHistoryAdmin)
admin.site.register(Language, SimpleHistoryAdmin)
