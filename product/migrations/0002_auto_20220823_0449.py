# Generated by Django 3.0.7 on 2022-08-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images', to='product.ProductImageFile'),
        ),
    ]