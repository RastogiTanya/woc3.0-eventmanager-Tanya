# Generated by Django 3.1.5 on 2021-01-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210116_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=70)),
                ('eventype', models.IntegerField()),
                ('regtype', models.CharField(max_length=20)),
                ('people', models.IntegerField(blank=True)),
            ],
        ),
    ]