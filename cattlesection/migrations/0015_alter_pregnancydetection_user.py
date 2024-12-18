# Generated by Django 5.0.2 on 2024-04-29 10:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattlesection', '0014_pregnancydetection'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregnancydetection',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pregnancy_detection_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
