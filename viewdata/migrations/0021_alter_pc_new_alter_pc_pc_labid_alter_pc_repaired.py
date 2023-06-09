# Generated by Django 4.0.4 on 2022-05-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0020_remove_pc_broken_pc_new_pc_repaired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='new',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='pc_labID',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='repaired',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
