# Generated by Django 3.2.5 on 2022-10-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_laptopproperties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
