# Generated by Django 4.0.4 on 2022-05-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0045_alter_brokenpc_problemtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokenpc',
            name='ProblemType',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware')], default='Software1', max_length=50),
        ),
    ]