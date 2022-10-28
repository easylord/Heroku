# Generated by Django 3.2.5 on 2022-09-18 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0006_products_reviews'),
        ('stores', '0003_remove_stores_revews'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
        migrations.RemoveField(
            model_name='stores',
            name='product',
        ),
        migrations.AddField(
            model_name='stores',
            name='product',
            field=models.ManyToManyField(null=True, to='product.Products'),
        ),
    ]