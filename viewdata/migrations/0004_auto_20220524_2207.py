# Generated by Django 3.2.5 on 2022-05-24 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0003_auto_20220524_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='PC',
        ),
        migrations.DeleteModel(
            name='BrokenPC',
        ),
        migrations.DeleteModel(
            name='Lab',
        ),
    ]
