# Generated by Django 3.2.5 on 2022-09-30 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0014_auto_20220930_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondchoice',
            name='phoneItems',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phoneItems', to='test.phoneitems'),
        ),
    ]