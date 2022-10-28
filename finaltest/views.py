from django.shortcuts import render
from .models import Album, LapiItems, MyProducts
from .serializers import AlbumSerializer, LaptopItemsSerializer, TheProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response 




# Create your views here.

class PollViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopItemsSerializer
    queryset = LapiItems.objects.all()
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    lookup_field = 'id'
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter
    # authentication_classes = (TokenAuthentication,)


    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices =   MyProducts.objects.all()
        serializer = TheProductSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
   # @parser_classes([MultiPartParser,FormParser])

    def choice(self, request, id=None):
        question = self.get_object()
        data = request.data
        data["prod_id"] = question.id
        serializer = TheProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    lookup_field = 'id'