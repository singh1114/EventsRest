# Import serializers from rest_framework
from rest_framework import serializers

# Import all the model classes
from .models import *

# make a model serializer class
class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventList
        fields = (
            'Event_Id',
            'Event_Name'
        )
