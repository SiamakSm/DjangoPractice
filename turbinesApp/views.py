from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TurbineModelSerializer


# Create your views here.

def healthh(request):
    return HttpResponse("healthh turbine")


class TurbineHealthView (APIView) : 
    def get(self, request):
        return Response ({"turbines_online": 3, "grid_connected": True},
            status=status.HTTP_200_OK)
    


class TurbineCreateView(APIView):
    def post(self, request):

        #name = request.data.get("name")
        #capacity = request.data.get("capacity_mw")

        #if not name or not capacity:
        #    return Response(
        #        {"error": "name and capacity_mw are required"},
        #        status=status.HTTP_400_BAD_REQUEST
        #    )

        #return Response(
        #    {"message": f"Turbine '{name}' received!", "capacity_mw": capacity},
        #    status=status.HTTP_201_CREATED
        #)

        serializer = TurbineModelSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)