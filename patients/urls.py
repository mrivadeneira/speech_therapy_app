from django.urls import path, include
from . import views

urlpatterns = [
    path('patients/',views.PatientsListAPIView.as_view()),
    path('patients/<int:pk>',views.PatientChangeAPIView.as_view()),
    path('sessions/',views.SessionsListAPIView.as_view()),
    path('sessions/<int:pk>',views.PatientSessionsAPIView.as_view()),
    path('details/',views.DetailsListAPIView.as_view()),
    path('details/<int:pk>',views.PatientDetailsAPIView.as_view()),
]
