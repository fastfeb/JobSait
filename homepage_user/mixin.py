from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse

class NoCompanyRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    login_url = '/accounts/login'
    redirect_company_url_name = 'some_company_dashboard_url'

    def test_func(self):
        return not hasattr(self.request.user, 'company') and self.request.company is not None

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(reverse(self.redirect_company_url_name))
        return super().handle_no_permission()
