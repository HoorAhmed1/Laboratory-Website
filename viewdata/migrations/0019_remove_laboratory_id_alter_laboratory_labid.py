# Generated by Django 4.0.4 on 2022-05-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0018_laboratory_id_alter_laboratory_labid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratory',
            name='id',
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='labID',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
