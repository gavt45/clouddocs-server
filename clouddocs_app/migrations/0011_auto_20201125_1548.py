# Generated by Django 3.1.3 on 2020-11-25 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clouddocs_app', '0010_auto_20201125_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='direction',
            new_name='id_direction',
        ),
    ]