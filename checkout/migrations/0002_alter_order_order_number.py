# Generated by Django 3.2.9 on 2021-12-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=40),
        ),
    ]
