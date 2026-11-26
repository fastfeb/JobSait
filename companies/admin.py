from django.contrib import admin
from .models import Company, Vacancy

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'website', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('owner__username', 'name')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'employment_type', 'schedule', 'created_at')
    list_filter = ('employment_type', 'schedule', 'created_at')
    search_fields = ('company__name', 'title')



