# Generated by Django 3.0.7 on 2020-07-11 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20200710_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
