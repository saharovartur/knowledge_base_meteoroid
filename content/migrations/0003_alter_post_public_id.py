# Generated by Django 5.1.2 on 2024-10-10 10:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_post_options_post_fixed_post_public_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='public_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
