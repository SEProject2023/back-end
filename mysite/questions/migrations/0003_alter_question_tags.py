# Generated by Django 3.2.19 on 2023-07-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20230701_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
