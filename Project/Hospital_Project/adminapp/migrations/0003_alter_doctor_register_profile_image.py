# Generated by Django 4.2.16 on 2024-11-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_doctor_register_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_register',
            name='profile_image',
            field=models.ImageField(upload_to='Media/Doctor Image/'),
        ),
    ]