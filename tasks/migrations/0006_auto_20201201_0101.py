# Generated by Django 3.1.3 on 2020-12-01 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20201201_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='github_link',
            field=models.CharField(default=None, max_length=200, verbose_name='GitHub Link'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('idea', 'Idea'), ('todo', 'TODO'), ('in_progress', 'In Progress'), ('completed', 'completed')], max_length=40, verbose_name='Status'),
        ),
    ]
