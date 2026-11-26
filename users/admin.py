from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_verified', 'created_at', 'location')
    list_filter = ('is_verified', 'created_at')
    search_fields = ('user__username', 'location', 'phone' )
