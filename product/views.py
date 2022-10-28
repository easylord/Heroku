from itertools import product
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from .models import Products, ProductImageFile, LaptopProperties
from .serializers import TweetSerializer, LaptopPropertiesSerializer
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, generics
from rest_framework.views import APIView



@api_view(['GET','POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def create_products(request):
    user = request.user

    if request.method == 'GET':
        detail = [{"id": detail.id, "name": detail.name, "description": detail.description, "price": detail.price, 'images': detail.images, "subCategory" : detail.subCategory, "owner": detail.owner, "likes": detail.likes, 'reviews':detail.reviews}
        for detail in Products.objects.all()]
        serializer = TweetSerializer(detail, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        files = request.FILES.getlist('images')
        if files:
            request.data.pop('images')

            serializer = TweetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                tweet_qs = Products.objects.get(id=serializer.data['id'])
                uploaded_files = []
                for file in files:
                    content = ProductImageFile.objects.create(media=file)
                    uploaded_files.append(content)

                tweet_qs.images.add(*uploaded_files)
                context = serializer.data
                context["images"] = [file.id for file in uploaded_files]
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TweetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()         
                context = serializer.data            
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def product_detail(request, id):
    try:
        transformer = Products.objects.get(id=id)
    except Products.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = TweetSerializer(transformer)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(transformer, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        transformer.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def topic_content_list(request, id):
    try:
        topic = LaptopProperties.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        contents = LaptopProperties.objects.filter(topic=topic)
        serializer = LaptopPropertiesSerializer(contents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data["product"] = product.id
        serializer = LaptopPropertiesSerializer(data=request.data)
        #print request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def LikeView(request, pk):
    post = get_object_or_404(Products, id=request.POST.get('post_id'))
    post.likes.add(request.user)

class LaptopViewSet(viewsets.ModelViewSet, APIView):
    serializer_class = LaptopPropertiesSerializer
    queryset = LaptopProperties.objects.all().order_by('product')
    lookup_field = 'id'
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter
    # authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        product = self.get_renderer_context()["request"].query_params.get('product')
        if product:
            return LaptopProperties.objects.filter(product=Products(product=product))[0:]

        else:
            return self.queryset
        
        return laptop

class LaptopDetailView(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)

    def get_object(self, id):
        try:
            return LaptopProperties.objects.get(id=id)
        except LaptopProperties.DoesNotExist as e:
            return Response( {"error": "Given question object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serailizer = LaptopPropertiesSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = LaptopPropertiesSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)

