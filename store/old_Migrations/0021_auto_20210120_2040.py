# Generated by Django 3.0.3 on 2021-01-20 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20210120_1625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorey',
            options={'verbose_name': 'Categorey Group', 'verbose_name_plural': 'Categorey Groups'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='Brand_image',
            field=models.ImageField(upload_to='brand/images', verbose_name='Brand Logo Image'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='Name',
            field=models.CharField(max_length=64, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='categorey',
            name='Name',
            field=models.CharField(help_text='Example - Schools, Classwise, Office, Pen and Pencils', max_length=64, verbose_name='Categorey Group Name'),
        ),
        migrations.AlterField(
            model_name='topbar',
            name='Name',
            field=models.CharField(help_text='Example - Newyear Topbar, New Session Topbar', max_length=256, verbose_name='Topbar Name'),
        ),
        migrations.AlterField(
            model_name='topbar_images',
            name='Image',
            field=models.ImageField(upload_to='genimages', verbose_name='Categorey Image'),
        ),
        migrations.AlterField(
            model_name='topbar_images',
            name='Name',
            field=models.CharField(help_text='Example - Markers, GK Books, Pencil Colors', max_length=48, verbose_name='Categorey Name'),
        ),
        migrations.CreateModel(
            name='SubCategorey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64, verbose_name='Categorey Name')),
                ('Parent_categorey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Subcategorey', to='store.Categorey', verbose_name='In Categorey Group')),
            ],
            options={
                'verbose_name': 'Product Categorey',
                'verbose_name_plural': 'Product Categories',
            },
        ),
    ]
