# Generated by Django 4.0.1 on 2022-02-02 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_patients_id_alter_patientscontact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientscontact',
            old_name='patient_id',
            new_name='patient',
        ),
    ]
