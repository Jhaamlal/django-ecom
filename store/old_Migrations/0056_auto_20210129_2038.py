# Generated by Django 3.0.3 on 2021-01-29 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0055_auto_20210129_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide_mob',
            name='GotoLink',
            field=models.URLField(blank=True, default='', verbose_name='Linked URL/Page'),
        ),
        migrations.AddField(
            model_name='slide_mob',
            name='Product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Slide_mob', to='store.Product'),
        ),
        migrations.AddField(
            model_name='slide_mob',
            name='ProductWithVariant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Slide_mob', to='store.ProductWithVariant'),
        ),
        migrations.AddField(
            model_name='slide_pc',
            name='GotoLink',
            field=models.URLField(blank=True, default='', verbose_name='Linked URL/Page'),
        ),
        migrations.AddField(
            model_name='slide_pc',
            name='Product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Slide_pc', to='store.Product'),
        ),
        migrations.AddField(
            model_name='slide_pc',
            name='ProductWithVariant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Slide_pc', to='store.ProductWithVariant'),
        ),
    ]