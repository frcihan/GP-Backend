# Generated by Django 3.1.5 on 2021-01-22 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gp_blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
