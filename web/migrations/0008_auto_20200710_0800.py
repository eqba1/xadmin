# Generated by Django 3.0.7 on 2020-07-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordresetcodes',
            name='email',
        ),
        migrations.AddField(
            model_name='passwordresetcodes',
            name='uid',
            field=models.CharField(default=9717023110, max_length=10),
            preserve_default=False,
        ),
    ]
