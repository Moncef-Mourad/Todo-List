# Generated by Django 4.2.6 on 2023-11-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0012_list_alter_todo_task_descr_alter_todo_task_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='svgColor',
            field=models.CharField(default='black', max_length=10),
        ),
    ]
