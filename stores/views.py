from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Stores
from .serializers import StoreSerializer
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
        detail = [{"id": detail.id, 'name':detail.name, 'adress':detail.adress, "description": detail.description, "owner": detail.owner, 'profile_image': detail.profile_image, 'delivery': detail.delivery,}
        for detail in Stores.objects.all()]        
        serializer = StoreSerializer(detail, many=True)
        return Response(serializer.data)

  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
# Create your views here.
@csrf_exempt
def transformer_detail(request, pk):
    try:
        transformer = Stores.objects.get(pk=pk)
    except Stores.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = StoreSerializer(transformer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(transformer, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        transformer.delete()
        return HttpResponse(status=204)