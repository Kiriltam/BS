# Generated by Django 2.2.7 on 2019-12-03 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20191203_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='people',
        ),
    ]