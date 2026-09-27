from django.urls import path
from . import views
from .views import TurbineHealthView, TurbineCreateView

urlpatterns = [
    path('health/', views.healthh),
    path('health_api/', TurbineHealthView.as_view(), name='turbine-health'),
    path('create/', TurbineCreateView.as_view(), name='create-turbine'),
]