from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from .models import  ProductImageFile, ProductImage
from .serializers import ProductImageSerializer, ProductImageFileSerializer

@api_view(['GET','POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])

def create_products(request):
    user = request.user

    if request.method == 'GET':
        detail = [{"id": detail.id, "name":detail.name, 'images': detail.images}
        for detail in ProductImageFile.objects.all()]
        serializer = ProductImageFileSerializer(detail, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        files = request.FILES.getlist('images')
        if files:
            request.data.pop('images')

            serializer = ProductImageFileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                tweet_qs = ProductImageFile.objects.get(id=serializer.data['id'])
                uploaded_files = []
                for file in files:
                    content = ProductImage.objects.create(media=file)
                    uploaded_files.append(content)

                tweet_qs.images.add(*uploaded_files)
                context = serializer.data
                context["images"] = [file.id for file in uploaded_files]
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ProductImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()         
                context = serializer.data            
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
