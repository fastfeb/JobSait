from django.contrib import admin
from .models import Company, Vacancy, FeedbackCompany, FavoriteVacancy
from communications.models import Response


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'website', 'created_at', 'average_rating_display')
    list_filter = ('created_at',)
    search_fields = ('owner__username', 'name')

    def average_rating_display(self, obj):
        return obj.average_rating()

    average_rating_display.short_description = "Средняя оценка"


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'employment_type', 'schedule', 'created_at')
    list_filter = ('employment_type', 'schedule', 'created_at')
    search_fields = ('company__name', 'title')


@admin.register(FeedbackCompany)
class FeedbackCompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'rating', 'id', 'created_at')
    list_filter = ('created_at', 'rating')
    search_fields = ('company__name', 'comment')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('vacancy', 'resume', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('vacancy__title', 'resume__last_name')

@admin.register(FavoriteVacancy)
class FavoriteVacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vacancy', 'created_at')
    search_fields = ('user__username', 'vacancy__title')
    list_filter = ('created_at',)



