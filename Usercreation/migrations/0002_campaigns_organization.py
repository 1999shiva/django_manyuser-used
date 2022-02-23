# Generated by Django 3.2.6 on 2022-02-22 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usercreation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaigns_name', models.CharField(max_length=20)),
                ('Organization_address', models.CharField(max_length=30)),
                ('Organization_city', models.CharField(max_length=30)),
                ('Organization_user', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campaigns_id', models.CharField(max_length=20)),
                ('Campaigns_name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='login_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
