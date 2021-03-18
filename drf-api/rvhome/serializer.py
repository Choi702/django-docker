from rest_framework import serializers
from .models import rvhome

class rvhomeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'title', 'specification', 'created_at')
        model = rvhome