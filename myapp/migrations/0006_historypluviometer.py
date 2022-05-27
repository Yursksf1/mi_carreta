# Generated by Django 3.2.4 on 2022-03-21 17:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_observations_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryPluviometer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('measure', models.PositiveIntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
