# Generated by Django 5.1 on 2024-09-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopManager', '0011_tbl_purchase_tbl_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_purchase',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
