# Generated by Django 3.2.5 on 2022-10-15 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_remove_stores_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stores',
            name='category',
        ),
    ]
