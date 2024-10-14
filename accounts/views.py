from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from accounts.models import Profile


class AccountsLoginView(LoginView):
    template_name = 'registration/login.html'


class AccountsLogoutView(LogoutView):
    pass


@login_required
def profile(request):
    profile_data = Profile.objects.all()
    return render(request, 'profile.html', {'profile_data': profile_data})