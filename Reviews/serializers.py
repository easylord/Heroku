from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id','rating', 'reviewed_by', 'description', 'num_of_rewiews', 'positive_likes', 'negative_likes' ]
        #fields = "__all__"