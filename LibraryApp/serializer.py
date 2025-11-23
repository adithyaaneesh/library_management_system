from rest_framework import serializers
from .models import Library
from Library.LibraryApp import models

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        models = Library
        fields = '__all__'