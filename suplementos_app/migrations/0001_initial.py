# Generated by Django 5.1.2 on 2024-11-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suplemento',
            fields=[
                ('id_producto', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=30)),
                ('sabor', models.CharField(max_length=15)),
                ('precio_uni', models.IntegerField()),
                ('peso', models.IntegerField()),
            ],
        ),
    ]
