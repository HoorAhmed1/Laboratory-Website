# Generated by Django 4.0.4 on 2022-05-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0038_computer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Computer',
        ),
        migrations.AddField(
            model_name='brokenpc',
            name='LabId',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
