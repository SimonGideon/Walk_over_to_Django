# Generated by Django 3.2.4 on 2021-07-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0006_alter_sales_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='sales',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
