# Generated by Django 3.1.1 on 2020-09-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycart', '0003_contect'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('items', models.CharField(default='', max_length=1000)),
                ('Name', models.CharField(default='', max_length=40)),
                ('Email', models.CharField(default='', max_length=40)),
                ('Address', models.CharField(default='', max_length=40)),
                ('City', models.CharField(default='', max_length=40)),
                ('State', models.CharField(default='', max_length=40)),
                ('Zip', models.CharField(default='', max_length=40)),
                ('Phone', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
