# Generated by Django 4.0.4 on 2022-05-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewdata', '0034_remove_pc_id_alter_pc_pcid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_labID', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
                ('repaired', models.BooleanField(default=False, null=True)),
                ('new', models.BooleanField(default=True, null=True)),
                ('pcID', models.DecimalField(decimal_places=0, max_digits=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='PC',
        ),
    ]