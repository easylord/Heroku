# Generated by Django 3.2.5 on 2022-09-20 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_products_likes'),
        ('subCategory', '0012_auto_20220919_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.products'),
        ),
    ]