from django.urls import path
from . import views
from .views import TurbineHealthView

urlpatterns = [
    path('health/', views.healthh),
    path('health_api/', TurbineHealthView.as_view(), name='turbine-health'),
]