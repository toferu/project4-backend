# Generated by Django 4.1.4 on 2023-01-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slammers_api', '0002_customer_order_product_video_delete_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, max_length=88, null=True),
        ),
    ]
