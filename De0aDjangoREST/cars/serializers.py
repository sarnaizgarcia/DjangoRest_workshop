from rest_framework import serializers

from .models import Brand


# herencia para adquirir datos del modelo
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', )
