# Generated by Django 5.0.2 on 2024-04-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CattleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=30)),
                ('species', models.CharField(choices=[('CATTLE', 'cattle'), ('BUFFALO', 'buffalo')], max_length=30)),
                ('breed', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('sireId', models.CharField(max_length=30)),
                ('damId', models.CharField(max_length=30)),
            ],
        ),
    ]
