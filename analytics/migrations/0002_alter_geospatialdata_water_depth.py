# Generated by Django 4.2.2 on 2025-02-09 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geospatialdata',
            name='water_depth',
            field=models.FileField(blank=True, null=True, upload_to='geospatial/waterdepthjson/'),
        ),
    ]
