# Generated by Django 5.1.1 on 2024-10-06 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_position_moderator'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalmodelprofile',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.position', verbose_name='Руководитель'),
        ),
    ]
