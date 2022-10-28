# Generated by Django 3.0.7 on 2022-08-27 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_things_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarksModel',
            fields=[
                ('Marksid', models.IntegerField(primary_key=True, serialize=False)),
                ('maths', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('computer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Studentmodel',
            fields=[
                ('stid', models.IntegerField(primary_key=True, serialize=False)),
                ('stname', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='thingsfile',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Things',
        ),
        migrations.DeleteModel(
            name='Thingsfile',
        ),
        migrations.AddField(
            model_name='marksmodel',
            name='stid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='things.Studentmodel'),
        ),
    ]