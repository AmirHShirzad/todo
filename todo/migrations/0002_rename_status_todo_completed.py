# Generated by Django 3.2.6 on 2022-08-15 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='status',
            new_name='completed',
        ),
    ]
