from django.db import models
from django.utils import timezone

class Response(models.Model):
    vacancy = models.ForeignKey('companies.Vacancy', on_delete=models.CASCADE, related_name='responses')
    resume = models.ForeignKey('resumes.Resume', on_delete=models.CASCADE, related_name='responses')
    cover_letter = models.TextField(blank=True, null=True)
    created_at = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50,
        choices=[
            ('new', 'новый'),
            ('accepted', 'принят'),
            ('viewed', 'просмотрен'),
            ('unaccepted', 'отклонён')
        ],
        default='new')
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        constraints = [
            models.UniqueConstraint(fields=['vacancy', 'resume'], name="unique_response_per_vacancy_resume")
        ]

    def __str__(self):
        return f'Отклик от {self.resume} на вакансию {self.vacancy}'


class Invitation(models.Model):
    vacancy = models.ForeignKey('companies.Vacancy', on_delete=models.CASCADE, related_name='invitations')
    resume = models.ForeignKey('resumes.Resume', on_delete=models.CASCADE, related_name='invitations')
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, 
        choices=[
            ('new', 'новое'),
            ('accept', 'принято'),
            ('rejected', 'отклонено')
        ],
        default='new')

    class Meta:
        verbose_name = "Приглашение"
        verbose_name_plural = "Приглашения"
        constraints = [
            models.UniqueConstraint(
                fields=["vacancy", "resume"],
                name="unique_invitation_per_vacancy_resume"
            )
        ]

    def __str__(self):
        return f"Приглашение на {self.vacancy} для {self.resume}"
