# Generated by Django 3.2.4 on 2022-02-06 21:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220206_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observations',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]