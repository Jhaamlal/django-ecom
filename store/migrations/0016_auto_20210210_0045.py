# Generated by Django 3.0.3 on 2021-02-09 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20210208_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='Father',
            field=models.CharField(blank=True, default='Not Applicable', max_length=164, verbose_name='(C/O) Gaurdian Name'),
        ),
    ]