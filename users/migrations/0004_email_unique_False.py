# Generated by Django 3.1.3 on 2020-11-28 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_email_unique'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together=set(),
        ),
    ]