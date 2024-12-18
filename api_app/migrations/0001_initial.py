# Generated by Django 5.1.3 on 2024-11-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_content', models.CharField(max_length=5000)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
