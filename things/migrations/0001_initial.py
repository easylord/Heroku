# Generated by Django 3.0.7 on 2022-08-22 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subCategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thingsfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(null=True, upload_to='images/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('images', models.ManyToManyField(related_name='images', to='things.Thingsfile')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subCategory.subCategory')),
            ],
            options={
                'verbose_name_plural': 'Things',
            },
        ),
    ]
