# Generated by Django 2.1.7 on 2019-03-17 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20190311_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_agent',
            name='image',
            field=models.ImageField(upload_to='product_image/'),
        ),
        migrations.AlterField(
            model_name='add_company',
            name='image',
            field=models.ImageField(upload_to='product_image/'),
        ),
        migrations.AlterField(
            model_name='customer_registration',
            name='image',
            field=models.ImageField(upload_to='product_image/'),
        ),
    ]
