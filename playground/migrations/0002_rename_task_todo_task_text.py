# Generated by Django 4.2.6 on 2023-10-24 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='Task',
            new_name='task_Text',
        ),
    ]
