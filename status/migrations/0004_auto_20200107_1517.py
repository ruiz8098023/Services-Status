# Generated by Django 2.0.5 on 2020-01-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_auto_20200107_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceshistory',
            name='notify_action',
            field=models.BooleanField(default=False, verbose_name='Field Caption'),
        ),
    ]