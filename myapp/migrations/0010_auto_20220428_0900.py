# Generated by Django 3.2.4 on 2022-04-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_group_historysheep_service_sheepgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='color',
        ),
        migrations.AlterField(
            model_name='group',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
