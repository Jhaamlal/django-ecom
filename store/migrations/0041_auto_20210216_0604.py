# Generated by Django 3.0.3 on 2021-02-16 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_auto_20210216_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CurrentShippingAddress',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Customer', to='store.ShippingAddress'),
        ),
    ]
