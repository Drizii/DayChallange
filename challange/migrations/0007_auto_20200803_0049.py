# Generated by Django 3.0.8 on 2020-08-02 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0006_auto_20200802_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='day',
            new_name='date',
        ),
    ]