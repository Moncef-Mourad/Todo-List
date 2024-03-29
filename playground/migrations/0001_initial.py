# Generated by Django 4.2.6 on 2023-12-07 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListName', models.CharField(default='Personal', max_length=10)),
                ('svgColor', models.CharField(default='black', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('due_date', models.DateField(default='0000-00-00')),
                ('task_Text', models.CharField(max_length=50)),
                ('task_Descr', models.CharField(default='Default Decription', max_length=150)),
                ('task_Progress', models.CharField(default='Incomplete', max_length=15)),
                ('isDone', models.BooleanField(default=False)),
                ('is_in_recycle_bin', models.BooleanField(default=False)),
                ('task_List', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModificationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_fields', models.JSONField()),
                ('modification_date', models.DateTimeField(auto_now_add=True)),
                ('original_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.todo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeletedTask',
            fields=[
                ('original_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='deleted_task', serialize=False, to='playground.todo')),
                ('deletion_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
