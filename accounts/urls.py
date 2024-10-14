from django.urls import path, include

from accounts import views
from accounts.views import AccountsLoginView

urlpatterns = [
    path('login/', AccountsLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),


]