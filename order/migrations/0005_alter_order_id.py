# Generated by Django 5.0.4 on 2024-08-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_set_initial_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
