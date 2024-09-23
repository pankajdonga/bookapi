from rest_framework import serializers
from .models import *

class bookSerial(serializers.ModelSerializer):
    class Meta:
        model=bookData
        fields='__all__'