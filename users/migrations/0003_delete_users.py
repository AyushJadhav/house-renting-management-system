# Generated by Django 4.2.11 on 2024-03-28 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
