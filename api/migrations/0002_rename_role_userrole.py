# Generated by Django 4.0.5 on 2022-07-24 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role',
            new_name='UserRole',
        ),
    ]