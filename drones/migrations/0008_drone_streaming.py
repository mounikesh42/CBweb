# Generated by Django 4.2.2 on 2024-07-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0007_dronedata_filefield_alter_dronedata_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='streaming',
            field=models.URLField(null=True),
        ),
    ]
