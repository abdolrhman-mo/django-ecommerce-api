# Generated by Django 5.0.4 on 2024-08-19 22:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_initial'),
        ('orderItem', '0002_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SingularProductOrder',
            new_name='OrderItem',
        ),
    ]
