# Generated by Django 3.2.5 on 2022-09-30 05:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0011_auto_20220929_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='secondchoice',
            name='phoneItems',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='test.phoneitems'),
        ),
        migrations.AlterField(
            model_name='phoneitems',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
