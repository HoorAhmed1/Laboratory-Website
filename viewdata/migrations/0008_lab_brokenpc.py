# Generated by Django 4.0.4 on 2022-05-24 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0007_auto_20220524_2231'),
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
                ('PC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewdata.pc')),
            ],
        ),
        migrations.CreateModel(
            name='BrokenPC',
            fields=[
                ('pcID', models.DecimalField(decimal_places=0, max_digits=6, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('softwareProblem', models.BooleanField(default=False)),
                ('hardwareProblem', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=150)),
                ('date', models.DateField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewdata.pc')),
            ],
        ),
    ]
