from rest_framework import serializers
from customer.models import Product, Customer


class Productserilizers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class Customerserilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

        def create(self, validated_data):
            return Customer.objects.create_user(**validated_data)
