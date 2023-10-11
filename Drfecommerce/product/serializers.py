from rest_framework import serializers
from .models import Product,Brand,Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializers()
    Category = CategorySerializers()
    class Meta:
        model = Product
        fields = "__all__"