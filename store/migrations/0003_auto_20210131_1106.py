# Generated by Django 3.0.3 on 2021-01-31 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210131_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_type',
            name='Product_type_attributes',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Customer',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
