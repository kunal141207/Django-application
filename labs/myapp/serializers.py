from rest_framework import serializers
from myapp.models import User, ActivityPeriod

#ActivityPeriod serializer
class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = '__all__'

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
        
#Results serializer
class ResultSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = [ 
            "id",
            "real_name",
            "tz",
            "activity_periods"
        ]


