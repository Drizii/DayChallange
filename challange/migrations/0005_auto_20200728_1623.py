# Generated by Django 3.0.8 on 2020-07-28 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0004_auto_20200728_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='condition',
        ),
        migrations.DeleteModel(
            name='Condition',
        ),
    ]
