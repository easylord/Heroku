# Generated by Django 3.2.5 on 2022-09-22 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subCategory', '0014_auto_20220922_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptopitems',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
