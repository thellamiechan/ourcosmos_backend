from rest_framework import serializers
from django.apps import apps

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('products.Product')
        fields ='__all__'