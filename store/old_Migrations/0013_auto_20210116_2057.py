# Generated by Django 3.0.3 on 2021-01-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210116_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterModelOptions(
            name='categorey',
            options={'verbose_name': 'Categorey', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='Tags',
            field=models.ManyToManyField(related_name='All_tags', to='store.Tag'),
        ),
    ]