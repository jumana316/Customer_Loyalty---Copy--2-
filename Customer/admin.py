from django.contrib import admin
from .forms import RewardAdminForm

# Register your models here.
from Customer.models import *

admin.site.register(User)
# admin.site.register(User)
class RewardAdmin(admin.ModelAdmin):
    form = RewardAdminForm

admin.site.register(Reward, RewardAdmin)
# admin.site.register(RewardCatalog)


