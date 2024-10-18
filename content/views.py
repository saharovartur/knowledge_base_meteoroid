import redis
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from content.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# связь с redis
r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


@login_required
def company_posts(request):
    current_user = request.user.profile
    current_company = current_user.company
    posts = Post.objects.filter(
        status='published',
        company=current_company).select_related('user', 'company', 'category')
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def post_detail(request, id):
    """Представление детальной инфо поста"""
    post = get_object_or_404(Post, pk=id)
    total_views = r.incr(f'post:{post.id}:views')  # incr увеличивает значение на 1
    return render(request, 'content/post_detail.html',
                  {'post': post,
                   'total_views': total_views})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


def about(request):
    return render(request, 'about.html')



