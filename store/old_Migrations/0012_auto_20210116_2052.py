# Generated by Django 3.0.3 on 2021-01-16 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20210116_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='TypeError',
            new_name='Type',
        ),
    ]
