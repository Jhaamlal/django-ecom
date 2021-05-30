# Generated by Django 3.0.3 on 2021-02-06 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210202_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Cart',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Customer', to='store.Cart'),
        ),
    ]
