# Generated by Django 4.0.6 on 2022-07-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Email_handler', '0002_remove_certificates_certificate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='cert_id',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
