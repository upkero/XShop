# Generated by Django 5.2 on 2025-05-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['id'], 'verbose_name': 'Item sold', 'verbose_name_plural': 'Items sold'},
        ),
    ]
