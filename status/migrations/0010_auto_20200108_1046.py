# Generated by Django 2.0.5 on 2020-01-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0009_servicehistorystatus_action_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicehistorystatus',
            name='action_notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
    ]