# Generated by Django 3.1.3 on 2020-11-28 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_bio_location_phone_null_blank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('email',)},
        ),
    ]
