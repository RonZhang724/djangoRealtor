# Generated by Django 2.2.2 on 2019-08-07 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='list_data',
            new_name='list_date',
        ),
    ]
