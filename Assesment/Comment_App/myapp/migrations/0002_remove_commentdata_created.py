# Generated by Django 5.1.1 on 2024-10-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentdata',
            name='created',
        ),
    ]
