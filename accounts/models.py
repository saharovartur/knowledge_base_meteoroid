from PIL import Image
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Главная модель профиля"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Сотрудник')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Компания',
                                blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL,
                                 blank=True, null=True, verbose_name='Должность', related_name='position')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL,
                                   blank=True, null=True, verbose_name='Отдел', related_name='department')
    supervisor = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name='Руководитель')
    education = models.TextField(verbose_name='Образование', blank=True)
    skills = models.TextField(verbose_name='Навыки', blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=11)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    date_of_employment = models.DateField(verbose_name='Дата трудоустройства', null=True, blank=True)
    date_of_dismissal = models.DateField(blank=True, null=True, verbose_name='Дата увольнения')
    fired = models.BooleanField(verbose_name='Уволен', null=True)
    notes = models.TextField(verbose_name='Примечания', blank=True)
    moderator = models.BooleanField(verbose_name='Модератор', null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Контактное лицо: {self.user.username} | Должность: {self.position}'


class Position(models.Model):
    """Модель должности"""
    title = models.CharField(verbose_name='Должность', unique=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Компания', blank=True, null=True)
    department = models.ForeignKey('Department', verbose_name='Отдел', on_delete=models.CASCADE,
                                   null=True, blank=True)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.title


class Department(models.Model):
    """Модель отделов"""
    title = models.CharField(verbose_name='Название отдела', max_length=100, unique=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name='Компания', blank=True, null=True)
    description = models.TextField(verbose_name='Описание отдела', blank=True)
    head = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='departments_headed', verbose_name='Руководитель')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Company(models.Model):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    title = models.CharField(verbose_name='Название компании', unique=True,
                             max_length=255)
    company_history = models.TextField(blank=True, verbose_name='История компании')
    description = models.TextField(verbose_name='Описание компании', blank=True)
    founded_date = models.DateField(verbose_name='Дата основания', blank=True, null=True)
    email = models.EmailField(verbose_name='Основной Email', unique=True)
    phone_number = models.CharField(verbose_name='Телефон', max_length=50)
    website = models.URLField(verbose_name='Сайт', blank=True)
    country = models.CharField(verbose_name='Страна', max_length=50, blank=True)
    city = models.CharField(verbose_name='Город главного офиса', max_length=100, blank=True)
    address = models.TextField(verbose_name='Юридический адрес', blank=True)
    employees_count = models.IntegerField(verbose_name='Количество сотрудников', default=0)
    legal_form = models.CharField(verbose_name='Юридическая форма', max_length=100, choices=[
        ('OOO', 'ООО'),
        ('ZAO', 'ЗАО'),
        ('PAO', 'ПАО'),
        ('IP', 'ИП'),], default='OOO')
    inn = models.CharField(verbose_name='ИНН', max_length=10, unique=True, blank=True)
    kpp = models.CharField(verbose_name='КПП', max_length=9, blank=True)
    ogrn = models.CharField(verbose_name='ОГРН', max_length=13, unique=True, blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)








