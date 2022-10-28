from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Review
from .serializers import ReviewSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response 


@api_view(['GET','POST']) 
@csrf_exempt
def transformer_list(request):
    """
    List all transformers, or create a new transformer
    """
    if request.method == 'GET':
        detail = [{"id": detail.id, 'rating':detail.rating, "description": detail.description, "reviewed_by": detail.reviewed_by, 'positive_likes': detail.positive_likes, 'negative_likes': detail.negative_likes}
        for detail in Review.objects.all()]        
        serializer = ReviewSerializer(detail, many=True)
        return Response(serializer.data)

  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# Create your views here.
