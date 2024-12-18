# Generated by Django 5.0.2 on 2024-04-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattlesection', '0005_alter_cattlemodel_breed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.IntegerField()),
                ('animal_code', models.CharField(blank=True, max_length=30, null=True)),
                ('body_weight', models.IntegerField(blank=True, null=True)),
                ('hearth_girth', models.IntegerField()),
                ('weight_date', models.CharField(max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
