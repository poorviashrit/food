from django.contrib import admin
from .models import Donation
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('food_name','donor_name','category','quantity','status','best_before')
    list_filter = ('category','status')
    search_fields = ('food_name','donor_name','pickup_location')
