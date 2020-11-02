from django.contrib import admin

from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput

from . models import Reviews


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'phone')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('phone',)}),
    )
    formfield_overrides = {
        NewUser.phone: {'widget': TextInput(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)

@admin.register(Reviews)
class AdminReviews(admin.ModelAdmin):
    list_display = ('user', 'expedition', 'comment', 'date')

