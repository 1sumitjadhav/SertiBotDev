# Generated by Django 4.0.6 on 2022-07-14 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Email_handler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificates',
            name='certificate_id',
        ),
    ]
