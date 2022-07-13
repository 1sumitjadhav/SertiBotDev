# Generated by Django 3.2.7 on 2022-07-12 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_rename_coupons_coupons1_coupons2'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupons1',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupons1',
            name='coupons2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='coupons1',
            name='discount',
            field=models.CharField(default='', max_length=100),
        ),
    ]