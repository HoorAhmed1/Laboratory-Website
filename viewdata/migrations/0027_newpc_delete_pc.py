# Generated by Django 4.0.4 on 2022-05-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0026_remove_pc_new2'),
    ]

    operations = [
        migrations.CreateModel(
            name='newPC',
            fields=[
                ('pc_labID', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('repaired', models.BooleanField(default=False, null=True)),
                ('new', models.BooleanField(default=True, null=True)),
                ('pc_ID', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='PC',
        ),
    ]
