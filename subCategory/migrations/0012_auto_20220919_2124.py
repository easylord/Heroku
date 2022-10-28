# Generated by Django 3.2.5 on 2022-09-19 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_alter_stores_product'),
        ('subCategory', '0011_auto_20220902_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashionitems',
            name='store_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.stores'),
        ),
        migrations.AddField(
            model_name='laptopitems',
            name='store_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.stores'),
        ),
        migrations.AddField(
            model_name='phoneitems',
            name='store_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.stores'),
        ),
    ]
