from django.contrib import admin
from .models import Resume, ResumeView

@admin.register(Resume)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'last_name', 'first_name', 'phone', 'desired_salary', 'created_at')
    fieldsets = (('Личные данные', 
        {'fields' : ('user', 'first_name', 'last_name', 'middle_name', 'gender', 'phone', 'date_of_birth')
    }),
    ('Желаемая зарплата', {'fields' : ('desired_salary', )}),
    ('Метаданные', {'fields': ('created_at', 'updated_at')}),
    )

    list_filter = ('gender', 'created_at')
    search_fields = ('last_name', 'first_name', 'phone', 'user__username')

@admin.register(ResumeView)
class ResumeViewAdmin(admin.ModelAdmin):
    list_display = ('company', 'resume', 'date')
    list_filter = ('company', 'date')
