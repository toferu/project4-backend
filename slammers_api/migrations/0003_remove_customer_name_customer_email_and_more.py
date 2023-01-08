# Generated by Django 4.1.4 on 2023-01-08 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slammers_api', '0002_customer_order_product_video_delete_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=75, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=72, null=True),
        ),
    ]