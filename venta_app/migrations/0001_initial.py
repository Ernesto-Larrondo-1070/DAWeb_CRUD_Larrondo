# Generated by Django 5.1.2 on 2024-11-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('id_prod', models.PositiveSmallIntegerField()),
                ('cliente', models.CharField(max_length=10)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('gr_kg', models.CharField(max_length=10)),
                ('servicios', models.CharField(max_length=100)),
            ],
        ),
    ]
