# Generated by Django 4.2.6 on 2023-10-24 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_alter_todo_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='isCompleted',
            new_name='isDone',
        ),
    ]