from django.contrib import admin
from .models import MpesaPayment


@admin.register(MpesaPayment)
class AdminMpesaPayment(admin.ModelAdmin):
    search_fields = ('description', 'payment_type')
    list_filter = ('created_at', 'payment_type')
    list_display = ('first_name', 'phone_number', 'amount')
