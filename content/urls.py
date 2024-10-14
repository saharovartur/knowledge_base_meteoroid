from django.urls import path

from content import views
from content.views import PostDetailView

urlpatterns = [
    path('', views.user_posts, name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),

]