# Generated by Django 3.1.3 on 2020-11-24 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clouddocs_app', '0005_auto_20201124_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id_protocol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clouddocs_app.protocol'),
        ),
    ]