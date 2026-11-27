from django.db import models
from django.contrib.auth.models import User
from .utils import company_logo_upload_path
from users.utils import validate_avatar_size
from professions.models import Profession
from django.conf import settings
from django.utils import timezone


class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.CharField(blank=True, null=True)
    logo = models.ImageField(upload_to=company_logo_upload_path, default='avatars/default.png', validators=[validate_avatar_size], blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        feedbacks = self.feedbacks.all()
        if feedbacks.exists():
            return round(sum(f.rating for f in feedbacks) / feedbacks.count(), 1)
        return 0

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_from = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    salary_to = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    experience = models.CharField(max_length=20, blank=True, null=True)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, related_name="vacancies", default='')
    city = models.CharField(max_length=50, unique=True,
    choices=[
        ('moscow', 'Москва'),
        ('saint_petersburg', 'Санкт-Петербург'),
        ('novosibirsk', 'Новосибирск'),
        ('yekaterinburg', 'Екатеринбург'),
        ('kazan', 'Казань'),
        ('krasnoyarsk', 'Красноярск'),
        ('nizhny_novgorod', 'Нижний Новгород'),
        ('chelyabinsk', 'Челябинск'),
        ('ufa', 'Уфа'),
        ('krasnodar', 'Краснодар'),
        ('samara', 'Самара'),
        ('rostov_on_don', 'Ростов-на-Дону'),
        ('omsk', 'Омск'),
        ('voronezh', 'Воронеж'),
        ('perm', 'Пермь'),
        ('volgograd', 'Волгоград'),
        ('saratov', 'Саратов'),
        ('tyumen', 'Тюмень'),
        ('tolyatti', 'Тольятти'),
        ('makhachkala', 'Махачкала'),
    ],
    default='moscow')
    street = models.CharField(max_length=256, blank=True, null=True)
    experience_required = models.CharField(max_length=50, unique=True,
        choices=[
            ('not_experience', 'Без опыта'),
            ('one_three_experience', 'Опыт 1-3 года'),
            ('four_five_experience', 'Опыт 4-5 лет'),
            ('more_six', 'Опыт более 6 лет')
        ],
        default='not_experience')
    salary_type = models.CharField(max_length=50, unique=True,
        choices=[
        ('weekly', 'Один раз в неделю'),
        ('monthly', 'Раз в месяц'), 
        ('two_monthly', 'Два раза в месяц'),
        ('daily', 'Ежедневно'),
        ('hours', 'По часам'),
        ('negotiable', 'Договорная')
        ],
        default='negotiable')
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


class FeedbackCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="feedbacks")
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class FavoriteVacancy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vacancy_favorite')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='in_favorite')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['vacancy', 'user'], name='unique_favorite_resume')
        ]
        verbose_name = 'Избранная вакансия'
        verbose_name_plural = 'Избранные вакансии'

        def __str__(self):
            return f'{self.user} добавил в избранные вакансию {self.vacancy}'

