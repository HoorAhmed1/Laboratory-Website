# Generated by Django 4.0.4 on 2022-05-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0029_remove_newpc_id_alter_newpc_pc_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newpc',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newpc',
            name='pc_ID',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True, unique=True),
        ),
    ]