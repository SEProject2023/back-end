# Generated by Django 3.2.19 on 2023-06-23 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatglmAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_model_answers', to='questions.question')),
            ],
        ),
    ]