# Generated by Django 5.1.1 on 2024-09-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0014_delete_tbl_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=30)),
                ('shop_email', models.CharField(max_length=30)),
                ('shop_details', models.CharField(max_length=30)),
                ('shop_password', models.CharField(max_length=30)),
                ('shop_photo', models.FileField(upload_to='Assets/Shop')),
            ],
        ),
    ]
