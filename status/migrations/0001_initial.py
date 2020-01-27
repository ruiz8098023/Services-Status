# Generated by Django 2.0.5 on 2019-12-13 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessService',
            fields=[
                ('business_service_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_service_name', models.CharField(max_length=100, unique=True)),
                ('business_service_description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Business Service',
                'verbose_name_plural': 'Business Services',
            },
        ),
        migrations.CreateModel(
            name='ServicesCategory',
            fields=[
                ('service_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=45, unique=True)),
                ('color', models.CharField(max_length=7, unique=True)),
            ],
            options={
                'verbose_name': 'Service Category',
                'verbose_name_plural': 'Services Category',
            },
        ),
        migrations.CreateModel(
            name='ServicesDescriptions',
            fields=[
                ('service_description_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=45)),
                ('business_service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.BusinessService')),
            ],
            options={
                'verbose_name': 'Services Description',
                'verbose_name_plural': 'Services Descriptions',
            },
        ),
        migrations.CreateModel(
            name='ServicesHistory',
            fields=[
                ('service_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.CharField(max_length=10, unique=True)),
                ('begin', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('action_description', models.TextField()),
                ('action_notes', models.TextField(blank=True, null=True)),
                ('closing_notes', models.TextField(blank=True, null=True)),
                ('notify_action', models.IntegerField()),
                ('business_service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.BusinessService')),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.ServicesCategory')),
            ],
            options={
                'verbose_name': 'Service History',
                'verbose_name_plural': 'Services History',
            },
        ),
        migrations.CreateModel(
            name='ServicesStatus',
            fields=[
                ('service_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'verbose_name': 'Service Status',
                'verbose_name_plural': 'Services Status',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('subscribers_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('business_service', models.ManyToManyField(to='status.BusinessService')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='SubscribersBusinessService',
            fields=[
                ('subscription_id', models.AutoField(primary_key=True, serialize=False)),
                ('business_service_key', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.BusinessService')),
                ('subscribers', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.Subscribers')),
            ],
        ),
        migrations.AddField(
            model_name='serviceshistory',
            name='service_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.ServicesStatus'),
        ),
        migrations.AlterUniqueTogether(
            name='servicesdescriptions',
            unique_together={('business_service', 'description')},
        ),
    ]