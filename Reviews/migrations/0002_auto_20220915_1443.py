# Generated by Django 3.2.5 on 2022-09-15 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='postive_experience',
            field=models.ManyToManyField(related_name='positive_experience', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
