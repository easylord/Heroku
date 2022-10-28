from rest_framework import serializers
from product.serializers import TweetSerializer
from .models import Cart
from authentication.serializers import RegisterSerializer




class CartSerializer(serializers.ModelSerializer):
    cart_id = serializers.ReadOnlyField(source='cart_id.username', read_only=False)

    #cart_id = RegisterSerializer(read_only=True, many=False)
    #books = BookSerializer(read_only=True, many=True)
    products = TweetSerializer(read_only=True, many=True)

    class Meta:
        model = Cart
        fields = ('cart_id', 'created_at', 'products')