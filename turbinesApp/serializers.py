from rest_framework import serializers
from .models import Alert , Turbine


class TurbinSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    capacity_mw = serializers.FloatField()
 

class TurbineModelSerializer(serializers.ModelSerializer):
    uppercase_name = serializers.SerializerMethodField()

    class Meta : 
        model = Turbine
        fields = '__all__' # or fields = ['name']

    def get_uppercase_name(self,obj) :
        return obj.name.upper()






class AlertSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(max_length=200)
    severity = serializers.CharField(max_length=20)


class AlertModelSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Alert
        fields = ['id','message','created_at']




class TurbineWithAlertsSerializer(serializers.ModelSerializer):
    alert_set = AlertModelSerializer(many=True, read_only=True)

    class Meta :
        model = Turbine
        fields = ['id','name','alert_set']

