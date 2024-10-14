from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from content.models import Post, Category


@admin.register(Post)
class PostAdmin(GuardedModelAdmin):
    list_display = ['user', 'company', 'title']


@admin.register(Category)
class CategoryAdmin(GuardedModelAdmin):
    list_display = ['company', 'title']
