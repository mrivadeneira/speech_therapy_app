# Generated by Django 4.0.1 on 2022-02-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_rename_patient_patientscontact_patient_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patientscontact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
