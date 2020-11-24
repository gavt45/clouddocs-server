# Generated by Django 3.1.3 on 2020-11-24 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clouddocs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='biomaterial',
            table='biomaterials',
        ),
        migrations.AlterModelTable(
            name='event',
            table='events',
        ),
        migrations.AlterModelTable(
            name='eventbiomaterials',
            table='event_biomaterials',
        ),
        migrations.AlterModelTable(
            name='eventfiles',
            table='event_files',
        ),
        migrations.AlterModelTable(
            name='eventtags',
            table='event_tags',
        ),
        migrations.AlterModelTable(
            name='eventtype',
            table='event_types',
        ),
        migrations.AlterModelTable(
            name='file',
            table='files',
        ),
        migrations.AlterModelTable(
            name='protocol',
            table='protocols',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tags',
        ),
    ]