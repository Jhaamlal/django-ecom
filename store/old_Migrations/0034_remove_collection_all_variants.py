# Generated by Django 3.0.3 on 2021-01-22 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0033_auto_20210123_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='All_variants',
        ),
    ]
