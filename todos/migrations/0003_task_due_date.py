# Generated by Django 4.2.3 on 2023-09-13 14:36

from django.db import migrations, models
import todos.models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_alter_task_options_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=todos.models.one_week_hence),
        ),
    ]