# Generated by Django 3.1.3 on 2020-11-24 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20201124_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='acquired',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.RemoveField(
            model_name='book',
            name='is_gift',
        ),
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
        migrations.RemoveField(
            model_name='book',
            name='published',
        ),
        migrations.RemoveField(
            model_name='book',
            name='reading_status',
        ),
    ]
