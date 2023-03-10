# Generated by Django 4.1.4 on 2023-01-06 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slammers_api', '0003_alter_product_description_alter_video_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('image', models.URLField(max_length=250, null=True)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Boards',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='boards',
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='slammers_api.goods'),
        ),
    ]
