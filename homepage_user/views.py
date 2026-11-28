from django.shortcuts import render
from django.views.generic import TemplateView
from companies.models import Vacancy
from core.models import SiteSettings
from communications.models import Response, Invitation
from django.db.models import Count
from companies.views import toggle_hidden_vacancy
from .utils import filtered_objects_with_filter_type




class HomePageView(TemplateView):
    template_name = 'homepage_user/homepage.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        filter_type = self.request.GET.get('filter')
        site_settings = SiteSettings.objects.first()
        context['logo'] = site_settings.logo if site_settings else None
        context['main_banner'] = site_settings.name_banner if site_settings else None
        total_response = Response.objects.count()
        total_invitations = Invitation.objects.count()
        context['total_response'] = total_response
        context['total_invitations'] = total_invitations
        vacancies = Vacancy.objects.select_related('company', 'profession').annotate(company_feedback_count=Count('company__feedbacks')).exclude(hidden_by_users__user=self.request.user)
        vacancies = filtered_objects_with_filter_type(vacancies, filter_type=filter_type)
        context['vacancies'] = vacancies[:8]


        return context






