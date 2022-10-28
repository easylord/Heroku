# from django.shortcuts import render

# Create your views here.

from itertools import product
from rest_framework import viewsets
from .serializers import ElectronicsSerializer, FashionItemsSerializer, FinalLinkSerializer, subCategorySerializer, ItemSubCategorySerializer, LaptopItemsSerializer, ElectronicsandMobilephonesAcessories
from .models import FashionItems, FinalLink, subCategory , ItemSubCategory, LaptopItems   
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from subCategory.models import LaptopItems, PhoneItems
from product.models import Products
from .serializers import  PhoneItemsSerializer, LaptopItemsSerializer
from django.views.generic.detail import DetailView
from django.utils import timezone
from rest_framework.decorators import api_view
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.views.generic.detail import DetailView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


class subCategoryViewsets(APIView):
    def get(self, request, format=None):
            snippets = subCategory.objects.all()
            serializer = subCategorySerializer(snippets, many=True)
            return Response(serializer.data)

class ItemSubCategoryViewsets(APIView):
    
    def get(self, request, format=None):
            snippets = ItemSubCategory.objects.all()
            serializer = ItemSubCategorySerializer(snippets, many=True)
            return Response(serializer.data)

# class LaptopItemsViewsets(APIView):

#     def get(self, request, format=None):
#             snippets = LaptopItems.objects.all()
#             serializer = LaptopItemsSerializer(snippets, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#             serializer = LaptopItemsSerializer(data=request.data, many=True)

#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return serializer.errors(status= status.HTTP_400_BAD_REQUEST)

class LaptopStudentapi(viewsets.ModelViewSet):
    queryset = LaptopItems.objects.all()
    serializer_class = LaptopItemsSerializer

              

class FinalLinkViewsets(APIView):
    queryset = FinalLink.objects.all()

    def get(self, request, format=None):
            snippets = FinalLink.objects.all()
            serializer = FinalLinkSerializer(snippets, many=True)
            return Response(serializer.data)

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="product__price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="product__price", lookup_expr='lte')

    class Meta:
        model = LaptopItems
        fields = "__all__"

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(products__price=value)
           
        )

@api_view(['GET'])
def showmultiplemodels(request):
    laptop= LaptopItems.objects.all()
    phone= PhoneItems.objects.all()
    fashion= FashionItems.objects.all()
    electronics = ElectronicsandMobilephonesAcessories.objects.all()
    filterset = ProductFilter(request.GET, queryset=laptop)
    if filterset.is_valid():
         queryset = filterset.qs
    laptopserializer = LaptopItemsSerializer(queryset, many=True)
    phoneserializer = PhoneItemsSerializer(phone, many = True)
    fashionserializer = FashionItemsSerializer(fashion, many=True)
    electronicsserializer = ElectronicsSerializer(electronics, many= True)
    finalserializer = laptopserializer.data + phoneserializer.data + fashionserializer.data + electronicsserializer.data

    return Response(finalserializer)
# def title_without_letter(queryset, request, *args, **kwargs):
#     letter_to_exclude = request.query_params['price']
#     return queryset(price__gte=letter_to_exclude)


class StandardPagesPagination(PageNumberPagination):
      page_size = 10



    

class ArticleDetailView(DetailView):
    model= LaptopItems.objects.all()
    model= PhoneItems.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



class EventDetailView(DetailView):
    model = LaptopItems


    # def get_object(self, queryset=None):
    #     return LaptopItems.objects.get(product=self.kwargs.get("product"))


    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        context['phone_items'] = PhoneItems.objects.all()

        return Response(context)

class TodoDetail(APIView):
    def get(self, request, product):
        todolaptop = get_object_or_404(LaptopItems.objects.all(), product__id = product)
        #todophone = get_object_or_404(PhoneItems.objects.all(), product__id = product)

        serializerlaptop = LaptopItemsSerializer(todolaptop,)
        #serializerphone = PhoneItemsSerializer(todophone,)
        #finalserializer = serializerlaptop.data + serializerphone.data

        return Response(serializerlaptop.data)

class TodoDetailphone(APIView):
    def get(self, request, product):
        todophone = get_object_or_404(PhoneItems.objects.all(), product__id = product)
        #todophone = get_object_or_404(PhoneItems.objects.all(), product__id = product)

        serializerphone = PhoneItemsSerializer(todophone,)
        #serializerphone = PhoneItemsSerializer(todophone,)
        #finalserializer = serializerlaptop.data + serializerphone.data

        return Response(serializerphone.data)