# Generated by Django 2.2.10 on 2020-04-13 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='interpreter',
        ),
    ]
