# Generated by Django 5.1.3 on 2024-11-26 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_alter_blogs_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_user',
            name='role',
        ),
    ]