# Generated by Django 3.1.3 on 2020-11-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clouddocs_app', '0004_auto_20201124_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id_direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clouddocs_app.direction'),
        ),
    ]
