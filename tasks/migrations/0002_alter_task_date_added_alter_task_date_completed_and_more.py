# Generated by Django 5.1.6 on 2025-02-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
