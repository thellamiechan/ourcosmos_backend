from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from django.http import Http404
from rest_framework import status, permissions


class ProductList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProductDetail(APIView):

    def get_object(self, pk):
        try:
          return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(
            instance=product,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()