from django.db import models


class CategoryProfession(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Profession(models.Model):
    category = models.ForeignKey(CategoryProfession, on_delete=models.CASCADE, related_name="professions")
    name = models.CharField(max_length=150, unique=True, verbose_name='Профессия')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return f'{self.name}'
