# Generated by Django 3.2.4 on 2022-03-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_historypluviometer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historypluviometer',
            name='create_at',
            field=models.DateField(),
        ),
    ]
