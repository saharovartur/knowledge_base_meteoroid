from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from content.models import Post

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def user_posts(request):
    current_user = request.user.profile
    current_company = current_user.company
    posts = Post.objects.filter(
        status='published',
        company=current_company).select_related('user', 'company', 'category')
    return render(request, 'post_list.html', {'posts': posts})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'


def about(request):
    return render(request, 'about.html')

