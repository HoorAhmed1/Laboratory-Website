# Generated by Django 4.0.4 on 2022-05-25 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0043_brokenpc_problemtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brokenpc',
            name='hardwareProblem',
        ),
        migrations.RemoveField(
            model_name='brokenpc',
            name='softwareProblem',
        ),
        migrations.AlterField(
            model_name='brokenpc',
            name='ProblemType',
            field=models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware')], default='Software1', max_length=20),
        ),
    ]
