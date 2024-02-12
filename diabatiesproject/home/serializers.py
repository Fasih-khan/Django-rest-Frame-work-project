from rest_framework import serializers
from .models import *
class DiabatiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diabetes
        fields = '__all__'
