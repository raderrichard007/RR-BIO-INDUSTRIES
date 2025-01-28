# Generated by Django 5.0.6 on 2024-09-30 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_member_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
