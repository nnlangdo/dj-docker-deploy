from django.contrib import admin
from .models import Donation
# Register your models here.

class DonationAdmin(admin.ModelAdmin):
    list_display = ('id','phone','name','address','mode_donation','amount','date_donation','cheque_no','cheque_micr','cheque_date','cheque_amount','draft_no','draft_micr','draft_date','draft_amount','created_by')
admin.site.register(Donation, DonationAdmin)
