# Generated by Django 5.1 on 2024-08-24 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_admregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=30)),
            ],
        ),
    ]
