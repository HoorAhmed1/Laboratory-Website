# Generated by Django 4.0.4 on 2022-05-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0015_laboratory_delete_lab_delete_newlab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratory',
            name='id',
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='labID',
            field=models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False),
        ),
    ]