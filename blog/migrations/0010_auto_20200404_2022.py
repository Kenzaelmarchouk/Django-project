# Generated by Django 3.0.2 on 2020-04-04 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200404_2017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formule',
            old_name='demand',
            new_name='demande',
        ),
        migrations.RenameField(
            model_name='formule',
            old_name='Full_name',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='formule',
            old_name='phone_number',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='formule1',
            old_name='bedroom_number',
            new_name='chambre',
        ),
        migrations.RenameField(
            model_name='formule1',
            old_name='demand',
            new_name='demande',
        ),
        migrations.RenameField(
            model_name='formule1',
            old_name='Full_name',
            new_name='nom',
        ),
    ]