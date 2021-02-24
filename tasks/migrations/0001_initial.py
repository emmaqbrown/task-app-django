# Generated by Django 3.1.3 on 2021-02-24 07:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('label', models.CharField(max_length=8)),
                ('notes', models.TextField()),
                ('due_date', models.DateField(verbose_name='Date Due')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date Created')),
                ('archive', models.BooleanField(default=False)),
            ],
        ),
    ]
