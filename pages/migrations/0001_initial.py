# Generated by Django 3.2.12 on 2022-03-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=32)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('vip_expiry', models.IntegerField()),
                ('user_type', models.SmallIntegerField(default=1)),
                ('is_login', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_time', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=128)),
                ('img_link', models.CharField(max_length=256)),
                ('video_url', models.CharField(max_length=256)),
            ],
        ),
    ]