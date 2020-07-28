# Generated by Django 3.0.8 on 2020-07-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challange', '0003_event_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=128, verbose_name='Warunek')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='condition',
        ),
        migrations.AddField(
            model_name='event',
            name='condition',
            field=models.ManyToManyField(blank=True, default=None, to='challange.Condition', verbose_name='Warunek'),
        ),
    ]