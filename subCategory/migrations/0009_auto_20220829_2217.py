# Generated by Django 3.0.7 on 2022-08-29 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220827_1944'),
        ('subCategory', '0008_laptopitems_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.Products'),
        ),
    ]
