# Generated by Django 2.2.13 on 2020-06-17 03:48

from django.db import migrations, models


def updates_score(apps, schema_editor):
    Package = apps.get_model('package', 'Package')
    for package in Package.objects.all():
        Package.objects.filter(pk=package.pk).update(score=package.calculate_score())


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0005_auto_20190927_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Score'),
        ),
        migrations.RunPython(updates_score)
    ]