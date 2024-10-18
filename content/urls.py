from django.urls import path

from content import views
from content.views import PostDeleteView

urlpatterns = [
    path('', views.company_posts, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', views.about, name='about'),

]