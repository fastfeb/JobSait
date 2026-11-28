from django.shortcuts import render, get_object_or_404
from .models import FavoriteVacancy, Vacancy, HiddenVacancy
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def toggle_favorite(request, vacancy_id):
    vacancy = get_object_or_404(vacancy, id=vacancy_id)
    favorite, created = FavoriteVacancy.objects.get_or_create(user=request.user, vacancy=vacancy)

    if not created:
        return JsonResponse({'status': 'removed'})
    
    return JsonResponse({'status': 'added'})


@login_required
@require_POST
def toggle_hidden_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        hidden, created = HiddenVacancy.objects.get_or_create(vacancy=vacancy, user=request.user)

        if not created:
            hidden.delete()
            return JsonResponse({'status': 'removed'})
        
        return JsonResponse({'status': 'hidden'})
    
    except Vacancy.DoesNotExist:
        return JsonResponse({'status': 'not found'}, status=404)


