# Generated by Django 3.1.3 on 2020-11-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20201126_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=None, max_length=256),
        ),
    ]
