from itertools import product
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from .models import Studentmodel, MarksModel
from .serializers import Studentserializer, Marksserializer 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import filters
from drf_multiple_model.views import ObjectMultipleModelAPIView
from subCategory.models import LaptopItems, PhoneItems
from subCategory.serializers import LaptopItemsSerializer, PhoneItemsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from .models import Products, ProductImageFile, LaptopItems, TheProducts, TheLaptopItems
from .serializers import   TheProductSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action


class Studentapi(viewsets.ModelViewSet):
    queryset = Studentmodel.objects.all()
    serializer_class = Studentserializer

class Marksapi(viewsets.ModelViewSet):
    queryset = MarksModel.objects.all()
    serializer_class = Marksserializer

class StandardPagesPagination(PageNumberPagination):
      page_size = 10


class SearchFilterView(ObjectMultipleModelAPIView):
    
    def get_querylist(self, request):
        paginator = PageNumberPagination()

        paginator.page_size = 10

        result_page = paginator.paginate_queryset(LaptopItems, request)
    querylist = (
        {'queryset': LaptopItems.objects.all(), 'serializer_class': LaptopItemsSerializer },
        {'queryset': PhoneItems.objects.all(), 'serializer_class': PhoneItemsSerializer},
    )

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ('product',)
    #paginator=StandardPagesPagination

@api_view(['GET','POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser,FormParser])
def create_products(request):
    user = request.user

    if request.method == 'GET':
        items = LaptopItems.objects.all()
        serializer = LaptopItemsSerializer(items, many=True)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     files = request.FILES.getlist('images')
    #     if files:
    #         request.data.pop('images')

    #         serializer = ProductSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             tweet_qs = Products.objects.get(id=serializer.data['id'])
    #             uploaded_files = []
    #             for file in files:
    #                 content = ProductImageFile.objects.create(media=file)
    #                 uploaded_files.append(content)

    #             tweet_qs.images.add(*uploaded_files)
    #             context = serializer.data
    #             context["images"] = [file.id for file in uploaded_files]
    #             return Response(context, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         serializer = ProductSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()         
    #             context = serializer.data            
    #             return Response(context, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    elif request.method == 'POST':
        serializer = LaptopItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

class PollViewSet(viewsets.ModelViewSet):
    serializer_class = LaptopItemsSerializer
    queryset = TheLaptopItems.objects.all()
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    lookup_field = 'id'
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter
    # authentication_classes = (TokenAuthentication,)


    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices =   TheProducts.objects.filter(question=question)
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