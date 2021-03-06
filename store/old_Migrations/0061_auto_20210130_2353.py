# Generated by Django 3.0.3 on 2021-01-30 18:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('store', '0060_slider_on_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Joined', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('Email', models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True)),
                ('PhoneNumber', models.CharField(help_text='10 Digit Phonenumber', max_length=10)),
                ('Gender', models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=6)),
                ('TotalPurchase', models.PositiveIntegerField(blank=True, default=0)),
                ('NumberOfOrders', models.PositiveSmallIntegerField(blank=True, default=0, editable=False)),
                ('ShoppedCategories', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=store.models.return_dict)),
                ('ShoppedSubCategories', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=store.models.return_dict)),
                ('ProfilePic', models.ImageField(blank=True, default='./static/store/images/avatar/avt.png', upload_to='profiles/profilepics')),
                ('Cart', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='Customer', to='store.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64, unique=True)),
                ('Created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='fileshare',
            name='File',
            field=models.FileField(blank=True, default=None, null=True, upload_to='fileshare/files'),
        ),
        migrations.AddField(
            model_name='fileshare',
            name='URL',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='fileshare',
            name='ImageFile',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='fileshare'),
        ),
        migrations.AlterField(
            model_name='fileshare',
            name='Text',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Father', models.CharField(max_length=164, verbose_name='(C/O) Gaurdian Name')),
                ('OwnerName', models.CharField(max_length=256)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('AltPhoneNumber', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=128, verbose_name='City/Town/Village')),
                ('Block', models.CharField(help_text='This is optional', max_length=128)),
                ('District', models.CharField(max_length=128)),
                ('PIN', models.CharField(max_length=6)),
                ('State', models.CharField(max_length=128)),
                ('LandMark', models.CharField(help_text='(Optional)', max_length=164)),
                ('AddressType', models.CharField(choices=[('HOME', 'HOME (All day delivery)'), ('WORK', 'Work/Office (From 10AM To 5PM)')], max_length=164)),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShippingAddressOptions', to='store.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveSmallIntegerField()),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Variant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='In_orders', to='store.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveSmallIntegerField()),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='In_orders', to='store.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('LastModified', models.DateTimeField(default=django.utils.timezone.now)),
                ('Status', models.CharField(choices=[('0', 'Pending'), ('1', 'Order Recived'), ('2', 'Declined By Seller'), ('3', 'Cancelation Requested'), ('4', 'Cancel Completed'), ('5', 'Packed & Bill Genrated'), ('6', 'Shipped Out'), ('7', 'On The Way'), ('8', 'Completed'), ('9', 'Declined By Buyer'), ('10', 'Return Requested'), ('11', 'Return Completed'), ('12', 'Disputed'), ('13', 'Verification Required')], default='0', max_length=64)),
                ('TotalPrice', models.PositiveIntegerField(editable=False)),
                ('SellerComments', models.TextField(default='No Comments From Seller!')),
                ('DaysForCompletion', models.PositiveSmallIntegerField(blank=True, default=None, editable=False, null=True)),
                ('FeedbackRating', models.PositiveSmallIntegerField(blank=True, default=None, editable=False, null=True)),
                ('FeedbackComment', models.TextField(blank=True, default=None, editable=False, max_length=600, null=True)),
                ('Categories', models.ManyToManyField(editable=False, related_name='In_orders', to='store.Categorey')),
                ('Customer', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Orders', to='store.Customer')),
                ('Method', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='Orders', to='store.PaymentMethod')),
                ('Products', models.ManyToManyField(editable=False, related_name='Orders', to='store.OrderProduct')),
                ('ShippingAddress', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='Orders', to='store.ShippingAddress')),
                ('SubCategories', models.ManyToManyField(editable=False, related_name='In_orders', to='store.SubCategorey')),
                ('Variants', models.ManyToManyField(editable=False, related_name='Orders', to='store.OrderVariant')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='CurrentShippingAddress',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Customer', to='store.ShippingAddress'),
        ),
        migrations.CreateModel(
            name='CartVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveSmallIntegerField()),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='In_carts', to='store.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveSmallIntegerField()),
                ('Added', models.DateTimeField(auto_now_add=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='In_carts', to='store.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='Product',
            field=models.ManyToManyField(related_name='Carts', to='store.CartProduct'),
        ),
        migrations.AddField(
            model_name='cart',
            name='Variant',
            field=models.ManyToManyField(related_name='Carts', to='store.CartVariant'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Email', models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True)),
                ('PhoneNumber', models.CharField(help_text='10 Digit Phonenumber', max_length=10)),
                ('Gender', models.CharField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=6)),
                ('Customer', models.OneToOneField(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='store.Customer')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
