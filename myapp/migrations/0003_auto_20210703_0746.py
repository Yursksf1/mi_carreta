# Generated by Django 3.2.4 on 2021-07-03 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_historyweather'),
    ]

    operations = [
        migrations.AddField(
            model_name='sheepphoto',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sheepphoto',
            name='is_principal',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='sheep',
            name='birthday',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
