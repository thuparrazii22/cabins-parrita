# Generated by Django 4.1.1 on 2022-12-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0002_alter_billdetail_correlative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_number',
            field=models.IntegerField(unique=True, verbose_name='Número de factura'),
        ),
    ]
