# Generated by Django 3.2.5 on 2022-10-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0007_alter_review_reviewed_by'),
        ('test', '0015_alter_secondchoice_phoneitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondchoice',
            name='reviews',
        ),
        migrations.AddField(
            model_name='secondchoice',
            name='reviews',
            field=models.ManyToManyField(related_name='Second_choicereviews', to='Reviews.Review'),
        ),
    ]
