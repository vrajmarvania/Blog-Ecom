# Generated by Django 3.1.1 on 2020-09-27 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0005_auto_20200927_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='items_json',
        ),
    ]
