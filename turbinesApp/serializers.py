from rest_framework import serializers
from .models import Alert , Turbine


class TurbinSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    capacity_mw = serializers.FloatField()
 

class TurbineModelSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Turbine
        fields = '__all__' # or fields = ['name']




class AlertSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(max_length=200)
    severity = serializers.CharField(max_length=20)


class AlertModelSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Alert
        fields = ['id','message','created_at']



