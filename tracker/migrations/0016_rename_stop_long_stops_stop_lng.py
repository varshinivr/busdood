# Generated by Django 4.1.3 on 2022-11-25 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0015_remove_route_end_lat_remove_route_end_long'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stops',
            old_name='stop_long',
            new_name='stop_lng',
        ),
    ]