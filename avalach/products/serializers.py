from rest_framework import serializers
from django.apps import apps

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('products.Product')
        fields ='__all__'

class ProductDetailSerializer(ProductSerializer):
    project=ProductSerializer(many=True)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('Title', instance.title)
        instance.author = validated_data.get('Author', instance.author)
        instance.synopsis = validated_data.get('Synopsis',instance.synopsis)
        instance.price = validated_data.get('Price', instance.price)
        instance.save()
        return instance
