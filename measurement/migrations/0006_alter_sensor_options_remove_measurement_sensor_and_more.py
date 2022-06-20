# Generated by Django 4.0.3 on 2022-03-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_measurement_sensor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={},
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='measurements',
            field=models.ManyToManyField(related_name='measurements', to='measurement.measurement'),
        ),
    ]
