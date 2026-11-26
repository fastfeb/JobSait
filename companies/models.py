from django.db import models
from django.contrib.auth.models import User
from .utils import company_logo_upload_path
from users.utils import validate_avatar_size

class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.CharField(blank=True, null=True)
    logo = models.ImageField(upload_to=company_logo_upload_path, default='avatars/default.png', validators=[validate_avatar_size], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    experience = models.CharField(max_length=20, blank=True, null=True)
    employment_type = models.CharField(
        max_length=50,
        choices=[
        ('full_time', 'Полная занятость'),
        ('part_time', 'Частичная занятость'),
        ('internship', 'Стажировка'),
        ('contract', 'Контракт'),
        ('remote', 'Удалённая работа')
        ], 
        default='full_time',
        ) 
    schedule = models.CharField(
        max_length=50,
        choices=[
            ("day", "Дневные смены"),
            ("night", "Ночные смены"),
            ("flexible", "Гибкий график"),
            ("shift", "Сменный график"),
            ("remote", "Удалённо"),
        ],
        default="day",
    )
    working_hours = models.CharField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} в {self.company.name}"
    

