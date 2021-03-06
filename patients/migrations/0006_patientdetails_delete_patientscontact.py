# Generated by Django 4.0.1 on 2022-02-03 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_rename_patient_id_patientscontact_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('mobile_1', models.PositiveBigIntegerField()),
                ('mobile_2', models.PositiveBigIntegerField()),
                ('zip_code', models.SmallIntegerField()),
                ('address_street', models.CharField(max_length=200)),
                ('address_floor', models.CharField(max_length=10)),
                ('address_ap', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patients')),
            ],
        ),
        migrations.DeleteModel(
            name='PatientsContact',
        ),
    ]
