# Generated by Django 3.2.4 on 2022-04-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20220428_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default='', max_length=100),
        ),
    ]
