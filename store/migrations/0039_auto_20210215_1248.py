# Generated by Django 3.0.3 on 2021-02-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_variant_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='Description',
            field=models.TextField(default='', editable=False),
        ),
    ]