# Generated by Django 2.2.7 on 2019-12-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20191205_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arrive',
            field=models.DateField(max_length=120, verbose_name='Дата Приезда'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='depart',
            field=models.DateField(max_length=120, verbose_name='Дата Отъезда'),
        ),
    ]
