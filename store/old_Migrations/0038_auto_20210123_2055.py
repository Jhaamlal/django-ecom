# Generated by Django 3.0.3 on 2021-01-23 15:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_auto_20210123_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='Brand_image',
        ),
        migrations.AddField(
            model_name='brand',
            name='Brand_image_cover',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='brand/images', verbose_name='Brand Logo Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='Brand_image_fill',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='brand/images', verbose_name='Brand Logo Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='Brand_image_fit',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='brand/images', verbose_name='Brand Logo Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='Brand_image_smart',
            field=imagekit.models.fields.ProcessedImageField(default='', upload_to='brand/images', verbose_name='Brand Logo Image'),
            preserve_default=False,
        ),
    ]
