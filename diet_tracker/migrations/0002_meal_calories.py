# Generated by Django 3.1 on 2020-08-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='calories',
            field=models.CharField(default=3, max_length=200),
            preserve_default=False,
        ),
    ]
