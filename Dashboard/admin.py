from django.contrib import admin
from .models import SaleAnalysis, ProfitAnalysis, TrxnAnalysis
from .forms import SalesForm, ProfitForm, TrxnForm
from import_export.admin import ImportExportModelAdmin


class SalesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    form = SalesForm
    list_display =("user","sale","add_date")
class TrxnAdmin(admin.ModelAdmin):
    form = TrxnForm
    list_display =("user","transactions")
    

admin.site.register(SaleAnalysis, SalesAdmin) 
admin.site.register(ProfitAnalysis)
admin.site.register(TrxnAnalysis,TrxnAdmin)