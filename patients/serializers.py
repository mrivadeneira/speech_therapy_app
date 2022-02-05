from rest_framework import serializers
from .models import Patients, PatientDetails, PatientSessions

class PatientSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSessions
        fields = ['patient','date','time','time',
                 'guardian','description']

class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = ['patient','email','mobile_1','mobile_2',
                 'zip_code','address_street','address_floor','address_ap']

class PatientsSerializer(serializers.ModelSerializer):
    sessions = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    details = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Patients
        fields = '__all__'
