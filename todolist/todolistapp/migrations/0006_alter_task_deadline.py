# Generated by Django 4.1.7 on 2023-02-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolistapp', '0005_task_deadline_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(null=True),
        ),
    ]
