# Generated by Django 4.0.3 on 2022-03-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0002_subcategory_initial_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]