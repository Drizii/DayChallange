# Generated by Django 3.0.8 on 2020-07-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0002_auto_20200728_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='condition',
            field=models.CharField(blank=True, default=None, max_length=128),
        ),
    ]
