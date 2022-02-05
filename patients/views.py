from .models import Patients, PatientDetails, PatientSessions
from .serializers import PatientsSerializer, PatientDetailsSerializer, PatientSessionsSerializer
from rest_framework import generics


class PatientsListAPIView(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class PatientChangeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class SessionsListAPIView(generics.ListCreateAPIView):
    queryset = PatientSessions.objects.all()
    serializer_class = PatientSessionsSerializer

class PatientSessionsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientSessions.objects.all()
    serializer_class = PatientSessionsSerializer

class DetailsListAPIView(generics.ListCreateAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer

class PatientDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientDetailsSerializer