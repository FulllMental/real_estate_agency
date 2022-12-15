# Generated by Django 2.2.24 on 2022-12-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20221212_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(blank=True, related_name='flats', to='property.Flat', verbose_name='Квартиры владельца'),
        ),
    ]
