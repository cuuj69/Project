# Generated by Django 2.2.7 on 2020-02-15 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('image', models.ImageField(upload_to='slider_img')),
                ('url', models.CharField(default='#', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dob', models.DateField(null=True)),
                ('photo', models.ImageField(default='default.png', upload_to='user_photos')),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('alternate_mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('landmark', models.CharField(blank=True, max_length=500, null=True)),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(choices=[('Northen Region', 'Northen Region'), ('Ashanti Region', 'Ashanti Region'), ('Western Region', 'Western Region'), ('Volta Region', 'Volta Region'), ('Eastern Region', 'Eastern Region'), ('Upper West Region', 'Upper West Region'), ('Upper East Region', 'Upper East Region'), ('Central Region', 'Central Region'), ('Bono East Region', 'Bono East Region'), ('Greater Accra Region', 'Greater Accra Region'), ('Savannah Region', 'Savannah Region'), ('North-East Region', 'North-East Region'), ('Oti Region', 'Oti Region'), ('Western North Region', 'Western North Region'), ('Ahafo Region', 'Ahafo Region'), ('Bono Region', 'Bono Region')], max_length=50, null=True)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100)),
                ('number', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
