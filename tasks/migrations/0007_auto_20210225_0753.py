# Generated by Django 3.1.3 on 2021-02-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_task_assigned_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.TextField(max_length=200),
        ),
    ]
