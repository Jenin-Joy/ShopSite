# Generated by Django 5.0.6 on 2024-09-22 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0016_alter_tbl_product_product_photo_and_more'),
        ('ShopManager', '0016_tbl_purchase_tbl_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(max_length=30)),
                ('usability', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShopManager.tbl_customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_product')),
            ],
        ),
    ]
