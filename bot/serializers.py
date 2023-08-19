from rest_framework import serializers
from .models import *

class MainSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    userText = serializers.CharField()
    assistantText = serializers.CharField()

class MessageTextModelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = MessageText
        fields = '__all__'


class SystemTextModalSerilaizer(serializers.ModelSerializer):
    
    class Meta:
        model = SystemTextModal
        fields = '__all__'