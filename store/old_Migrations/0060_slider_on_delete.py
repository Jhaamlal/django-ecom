# Generated by Django 3.0.3 on 2021-01-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0059_auto_20210130_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='On_delete',
            field=models.BooleanField(blank=True, default=False, editable=False),
        ),
    ]
