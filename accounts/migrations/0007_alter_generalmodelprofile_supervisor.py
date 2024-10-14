# Generated by Django 5.1.1 on 2024-10-06 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_generalmodelprofile_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalmodelprofile',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.generalmodelprofile', verbose_name='Руководитель'),
        ),
    ]
