# Generated by Django 4.0.4 on 2022-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0030_newpc_id_alter_newpc_pc_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpc',
            name='pc_ID',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]