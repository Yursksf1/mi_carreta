# Generated by Django 3.2.4 on 2021-07-05 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sheepphoto',
            options={'ordering': ['-is_principal']},
        ),
        migrations.AlterField(
            model_name='sheepbreed',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breed', to='myapp.breed'),
        ),
        migrations.AlterField(
            model_name='sheepbreed',
            name='sheep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sheep', to='myapp.sheep'),
        ),
    ]
