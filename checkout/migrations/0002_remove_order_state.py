# Generated by Django 3.2.9 on 2021-11-16 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]
