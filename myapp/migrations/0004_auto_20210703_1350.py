# Generated by Django 3.2.4 on 2021-07-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210703_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='acronym',
            field=models.CharField(default='HS', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breed',
            name='color',
            field=models.CharField(default='blue', max_length=100),
            preserve_default=False,
        ),
    ]
