# Generated by Django 5.1.2 on 2024-10-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_company_photo_department_photo_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_employment',
            field=models.DateField(blank=True, null=True, verbose_name='Дата трудоустройства'),
        ),
    ]