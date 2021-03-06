# Generated by Django 3.0.3 on 2021-01-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20210122_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Is_normal_product',
            field=models.BooleanField(blank=True, default=False, editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='Is_variant_product',
            field=models.BooleanField(blank=True, default=True, editable=False),
        ),
        migrations.AddField(
            model_name='productwithvariant',
            name='Is_normal_product',
            field=models.BooleanField(blank=True, default=False, editable=False),
        ),
        migrations.AddField(
            model_name='productwithvariant',
            name='Is_variant_product',
            field=models.BooleanField(blank=True, default=True, editable=False),
        ),
    ]
