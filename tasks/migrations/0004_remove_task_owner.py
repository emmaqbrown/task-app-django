# Generated by Django 3.1.3 on 2021-02-24 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
    ]