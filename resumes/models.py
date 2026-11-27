from django.db import models
from django.contrib.auth.models import User
from professions.models import Profession
from django.utils import timezone
from companies.models import Company


class Resume(models.Model):
    GENDER_CHOICES = [
        ("male", "Мужской"),
        ("female", "Женский"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    desired_salary = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="resumes", default='')

    def __str__(self):
        return f'Резюме: {self.last_name} {self.first_name}'


class ResumeView(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='resume_views')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='views')
    date = models.DateField(auto_now_add=timezone.now)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['company', 'resume', 'date'], name="unique_resume_view_per_day")
        ]
        verbose_name = 'Просмотр резюме'
        verbose_name_plural = 'Просмотры резюме'

    def __str__(self):
        return f'Просмотрел {self.company.name} резюме {self.resume} в {self.date}'

    
