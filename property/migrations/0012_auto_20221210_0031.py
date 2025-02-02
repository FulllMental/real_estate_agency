# Generated by Django 2.2.24 on 2022-12-09 21:31

from django.db import migrations


def fill_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all().iterator()
    for owner in owners:
        owner.flat.set(Flat.objects.filter(owner=owner.owner))


def move_backwards(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flat.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20221210_0031'),
    ]

    operations = [
        migrations.RunPython(fill_owners, move_backwards)
    ]