# In serializers.py
from rest_framework import serializers
from .models import Item

# class InjuryPredictSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         # fields = '__all__'
#         fields=['image']

class InjuryPredictSerializer(serializers.Serializer):
    AnimalImage = serializers.ImageField()
