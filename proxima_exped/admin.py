from django.contrib import admin
from .models import Expedition


@admin.register(Expedition)
class AdminExpedition(admin.ModelAdmin):
    search_fields = ('description', 'title')
    list_filter = ('date',)
    list_display = ('title', 'date', 'person_price')
