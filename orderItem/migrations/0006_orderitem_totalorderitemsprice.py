# Generated by Django 5.0.4 on 2024-08-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderItem', '0005_rename_gathered_orders_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='totalOrderItemsPrice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
