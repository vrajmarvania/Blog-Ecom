# Generated by Django 3.1.1 on 2020-09-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0006_auto_20200928_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items_json',
            field=models.CharField(max_length=5000),
        ),
    ]
