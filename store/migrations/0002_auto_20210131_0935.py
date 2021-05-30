# Generated by Django 3.0.3 on 2021-01-31 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='PhoneNumber',
        ),
        migrations.AddField(
            model_name='customer',
            name='Customer',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]