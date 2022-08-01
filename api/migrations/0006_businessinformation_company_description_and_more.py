# Generated by Django 4.0.5 on 2022-07-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_is_solution_seeker_user_is_solution_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinformation',
            name='company_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='businessinformation',
            name='company_website',
            field=models.URLField(blank=True, null=True),
        ),
    ]