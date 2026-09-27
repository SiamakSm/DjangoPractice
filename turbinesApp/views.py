from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def healthh(request):
    return HttpResponse("healthh turbine")


class TurbineHealthView (APIView) : 
    def get(self, request):
        return Response ({"turbines_online": 3, "grid_connected": True},
            status=status.HTTP_200_OK)