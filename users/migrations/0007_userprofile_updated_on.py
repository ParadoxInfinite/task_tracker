# Generated by Django 3.1.3 on 2020-12-01 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201130_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated On'),
        ),
    ]