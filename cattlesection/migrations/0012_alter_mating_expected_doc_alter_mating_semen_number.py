# Generated by Django 5.0.2 on 2024-04-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattlesection', '0011_mating_animal_code_mating_expected_doc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mating',
            name='expected_doc',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='mating',
            name='semen_number',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
