# Generated by Django 3.1.5 on 2021-01-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210124_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants',
            name='eventype',
            field=models.CharField(max_length=30),
        ),
    ]
