# Generated by Django 2.1.7 on 2019-07-16 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20190716_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='areas',
            new_name='area',
        ),
    ]
