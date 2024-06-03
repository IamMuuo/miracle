from rest_framework import serializers
from .models import MIRFileModel


class MIRModelFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MIRFileModel
        fields = "__all__"
