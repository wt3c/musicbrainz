# Generated by Django 2.1.7 on 2019-07-16 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20190716_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='genders',
            new_name='gender',
        ),
    ]
