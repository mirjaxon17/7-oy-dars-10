# Generated by Django 5.0.4 on 2024-05-17 01:00

import django.db.models.deletion
import products.helpers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to=products.helpers.SaveMediaFiles.category_img_path)),
                ('how_many', models.IntegerField(default=10)),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=products.helpers.SaveMediaFiles.sponser_img_path)),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=products.helpers.SaveMediaFiles.product_img_path)),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('$', 'USD'), ('UZS', "so'm")], default='UZS', max_length=10)),
                ('sale_price', models.FloatField(null=True)),
                ('reyting', models.FloatField(default=0)),
                ('how_many', models.IntegerField(default=2)),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='products.category')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Corzine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
