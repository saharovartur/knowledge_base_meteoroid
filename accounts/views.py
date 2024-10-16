from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from accounts.forms import UserRegistrationForm
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




@login_required
def register(request):
    """Вью регистрации"""
    user = request.user
    company_request_user = user.profile.company
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            Profile.objects.create(user=new_user, company=company_request_user)
            context = {'new_user': new_user}
            return render(request, 'accounts/register_done.html', context)

    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

