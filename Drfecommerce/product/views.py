from django.shortcuts import render
from rest_framework import viewsets
from .models import Category,Brand,Product
from rest_framework.response import Response
from .serializers import CategorySerializers,BrandSerializers,ProductSerializers
from drf_spectacular.utils import extend_schema

# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """Viewset for viewing all Category"""
    queryset = Category.objects.all()
    
    @extend_schema(responses=CategorySerializers)
    def list(self, request):
        serializer = CategorySerializers(self.queryset, many=True)
        return Response(serializer.data) 
    
class BrandViewSet(viewsets.ViewSet):
    """Viewset for viewing all Brands"""
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializers)
    def list(self, request):
        serializer = BrandSerializers(self.queryset, many=True)
        return Response(serializer.data) 
    
class ProductViewSet(viewsets.ViewSet):
    """Viewset for viewing all Products"""
    queryset = Product.objects.all()
    
    @extend_schema(responses=ProductSerializers)
    def list(self, request):
        serializer = ProductSerializers(self.queryset, many=True)
        return Response(serializer.data) 