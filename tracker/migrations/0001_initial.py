# Generated by Django 4.0.3 on 2022-03-24 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('product', models.TextField(blank=True, null=True)),
                ('initial_price', models.FloatField(blank=True, null=True)),
                ('new_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'price_change',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('idtracker', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_id', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'tracker',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserTracker',
            fields=[
                ('iduser_tracker', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('tracker_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'user_tracker',
                'managed': True,
            },
        ),
    ]
