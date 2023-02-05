from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

# from import_export import resources
# from import_export.admin import ImportMixin


# Register your models here.
admin.site.register(OtherFeeCharges, SimpleHistoryAdmin)
admin.site.register(Fee, SimpleHistoryAdmin)
admin.site.register(Payment, SimpleHistoryAdmin)
admin.site.register(Expense, SimpleHistoryAdmin)
