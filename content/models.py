import uuid
from django.contrib.auth.models import User
from django.db import models
from accounts.models import Company


class Category(models.Model):
    """Модель категории постов"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', related_name='category_company',
                                null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание категории', max_length=300)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель постов"""

    STATUS_OPTIONS = \
        (('draft', 'Черновик'), ('published', 'Опубликован'))

    public_id = models.UUIDField(db_index=True, unique=True,
                                 default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор',
                             related_name='user_post', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания', related_name='company_post',
                                null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE, related_name='posts',
                                 null=True, blank=True)

    update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL,
                                null=True, related_name='updater_posts', blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    status = models.CharField(choices=STATUS_OPTIONS, default='published',
                              verbose_name='Статус записи', max_length=10)
    fixed = models.BooleanField(verbose_name='Прикреплено', default=False)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пост {self.title} компании {self.company}'


