# Generated by Django 3.0.3 on 2021-02-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0046_auto_20210216_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='ForLater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cartvariant',
            name='ForLater',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='Status',
            field=models.CharField(choices=[('-1', 'Error'), ('0', 'Placed'), ('1', 'Order Recived'), ('2', 'Declined By Seller'), ('3', 'Cancelation Requested'), ('4', 'Cancel Completed'), ('5', 'Packed & Bill Genrated'), ('6', 'Shipped Out'), ('7', 'On The Way'), ('8', 'Completed'), ('9', 'Declined By Buyer'), ('10', 'Return Requested'), ('11', 'Return Completed'), ('12', 'Disputed'), ('13', 'Verification Required')], default='0', max_length=64),
        ),
    ]
