# Generated by Django 3.0.7 on 2022-09-02 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220827_1944'),
        ('subCategory', '0010_phoneitems_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsandautomobile',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carsproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='electronicsandmobilephonesacessories',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electronicsproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='fashionitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fashionproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='foodanddrinks',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foodproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='furnitureandappliacnes',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='furnituresproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='healthandbeauty',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='healthproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='housesandproperties',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houseproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='housingandhotelrent',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='housingproducts', to='product.Products'),
        ),
        migrations.AddField(
            model_name='jobsandskills',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobproducts', to='product.Products'),
        ),
        migrations.AlterField(
            model_name='laptopitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laptopproduct', to='product.Products'),
        ),
        migrations.AlterField(
            model_name='phoneitems',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phoneproducts', to='product.Products'),
        ),
    ]