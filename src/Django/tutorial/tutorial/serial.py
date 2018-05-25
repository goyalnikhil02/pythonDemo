from rest_framework import status
from rest_framework import serializers
from .models import Language

class LangSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Language
        fields = ('paradigm', 'name')
    