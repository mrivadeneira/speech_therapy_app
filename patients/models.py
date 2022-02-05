from django.db import models

class Patients(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    
class PatientDetails(models.Model):
    patient = models.ForeignKey(
        'patients.Patients',
        related_name='details',
        on_delete=models.CASCADE,
    )
    email = models.EmailField(max_length=254)
    mobile_1 = models.PositiveBigIntegerField()
    mobile_2 = models.PositiveBigIntegerField()
    zip_code = models.SmallIntegerField()
    address_street = models.CharField(max_length=200)
    address_floor = models.CharField(max_length=10)
    address_ap = models.CharField(max_length=200)

class PatientSessions(models.Model):
    patient = models.ForeignKey(
        'patients.Patients',
        related_name='sessions',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    time = models.TimeField()
    class Guardian(models.IntegerChoices):
        NO = 1
        YES = 2
    guardian = models.IntegerField(choices=Guardian.choices)
    description = models.TextField()
