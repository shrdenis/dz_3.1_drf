from django.urls import path

from .views import MeasurementCreateView, SensorListCreateView, SensorRetrieveUpdateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
