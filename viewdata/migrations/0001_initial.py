# Generated by Django 3.2.5 on 2022-05-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('labName', models.CharField(max_length=45)),
                ('labID', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('buildingNum', models.DecimalField(decimal_places=0, max_digits=3)),
                ('floorNum', models.DecimalField(decimal_places=0, max_digits=3)),
                ('numOfPC', models.DecimalField(decimal_places=0, max_digits=3)),
                ('numberOfChair', models.DecimalField(decimal_places=0, max_digits=3)),
                ('labCapacity', models.DecimalField(decimal_places=0, max_digits=4)),
                ('Status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcNumber', models.DecimalField(decimal_places=0, max_digits=6)),
                ('softwareProblem', models.BooleanField(default=False)),
                ('hardwareProblem', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=150)),
                ('date', models.DateField()),
                ('pcID', models.DecimalField(decimal_places=0, max_digits=10)),
                ('newPC', models.CharField(max_length=10)),
                ('repairedPC', models.CharField(max_length=10)),
            ],
        ),
    ]
