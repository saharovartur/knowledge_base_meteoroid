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
    current_user = request.user.profile
    profile_data = (Profile.objects.select_related('user', 'company',
                                                   'position',
                                                   'department', 'supervisor').filter(user__profile=current_user))
    return render(request, 'profile.html', {'profile_data': profile_data})


def register(request):
    pass