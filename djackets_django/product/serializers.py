from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "get_absolute_url",
            "price",
            "get_image_url",
            "get_thumbnail_url"
        )


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

    def get_products(self, category):
        products = category.product_set.all()
        return ProductSerializer(products, many=True).data
