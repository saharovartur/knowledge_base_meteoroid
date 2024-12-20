# Generated by Django 5.1.1 on 2024-10-04 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='position',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='position',
            name='department',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department', verbose_name='Отдел'),
        ),
    ]
