# Generated by Django 4.0.4 on 2022-05-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0028_newpc_id_alter_newpc_pc_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newpc',
            name='id',
        ),
        migrations.AlterField(
            model_name='newpc',
            name='pc_ID',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
