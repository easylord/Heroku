from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Category, PhoneItems, Product, ProductSpecificationValue, Choice, Question , SecondChoice
from rest_framework import viewsets, generics
from .serializers import CategorySerializer, PhoneItemsSerializer , ProductSerializer, ProductSpecificationValueSerializer, ChoiceSerializer, QuestionSerializer, SecondChoiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from product.models import ProductImageFile



@api_view(['GET','POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def create_products(request):
    user = request.user

    if request.method == 'GET':
        detail = [{"id": detail.id, "name": detail.name, "description": detail.description, "price": detail.price, 'images': detail.images, "subCategory" : detail.subCategory, "owner": detail.owner, "likes": detail.likes, 'reviews':detail.reviews}
        for detail in SecondChoice.objects.all()]
        serializer = SecondChoiceSerializer(detail, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        files = request.FILES.getlist('images')
        if files:
            request.data.pop('images')

            serializer = SecondChoiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                tweet_qs = SecondChoice.objects.get(id=serializer.data['id'])
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
            serializer = SecondChoiceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()         
                context = serializer.data            
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)



def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "store/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "store/single.html", {"product": product})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.root_nodes()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CategorySerializer

class LaptopItemsViewsets(APIView):

    def get(self, request, format=None):
            snippets = Product.objects.all()
            serializer = ProductSerializer(snippets, many=True)
            return Response({"laptopItems":serializer.data})

class TestItemsViewsets(APIView):

    def get(self, request, format=None):
            snippets = ProductSpecificationValue.objects.all()
            serializer = ProductSpecificationValueSerializer(snippets, many=True)
            return Response({"laptopItems":serializer.data})

class PollViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = 'id'
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter
    # authentication_classes = (TokenAuthentication,)


    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def choice(self, request, id=None):
        question = self.get_object()
        data = request.data
        data["question"] = question.id
        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)

class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneItemsSerializer
    queryset = PhoneItems.objects.all()
    lookup_field = 'id'
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter
    # authentication_classes = (TokenAuthentication,)


    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        question = self.get_object()
        choices = Choice.objects.filter(question=question)
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def choice(self, request, id=None):
        question = self.get_object()
        data = request.data
        data["question"] = question.id
        serializer = ChoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)

class PollDetailView(APIView):
    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response( {"error": "Given question object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serailizer = QuestionSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)


class Products(APIView):

    def get(self, request, format=None):
        products = PhoneItems.objects.all()
        serializer = PhoneItemsSerializer(products, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PhoneItemsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhonetestViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneItemsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        phone = PhoneItems.objects.all()
        return phone

    def create(self, request, *args, **kwargs):
        data= request.data
        new_phone = PhoneItems.objects.create(brand=data["brand"],model=data["model"],processor=data["processor"],condition=data["condition"],ram=data["ram"],storage_capacity=data["storage_capacity"],created_by=data["created_by"],operating_system=data["operating_system"],color=data["color"],sim=data["sim"],battery=data["battery"],item_subcategory=data["item_subcategory"],camera=data["camera"],store_info=data["store_info"])
        new_phone.save()
        for details in data["details"]:
            details_obj= SecondChoice.objects.get(text = details["text"], name = details["name"], description=details["description"])
            new_phone.details.add(details_obj)

        serializer = PhoneItemsSerializer(new_phone)
        return Response(serializer.data)

class PhoneViewSet(viewsets.ModelViewSet, APIView):
    serializer_class = PhoneItemsSerializer
    queryset = PhoneItems.objects.all()
    lookup_field = 'id'
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    # filter_backends = (DjangoFilterBackend,)
    # filter_class = PollFilter
    # authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        phone = PhoneItems.objects.all()
        return phone

    # def create(self, request, *args, **kwargs):
    #     data= request.data
    #     new_phone = PhoneItems.objects.create(brand=data["brand"],model=data["model"],processor=data["processor"],condition=data["condition"],ram=data["ram"],storage_capacity=data["storage_capacity"], operating_system=data["operating_system"],color=data["color"],sim=data["sim"],battery=data["battery"],camera=data["camera"])
    #     new_phone.save()
    #     for details in data["details"]:
    #         details_obj= SecondChoice.objects.get_or_create(text = details["text"], name = details["name"], description=details["description"])
    #         new_phone.details.add(details_obj)

    #     serializer = PhoneItemsSerializer(new_phone)
    #     return Response(serializer.data)

class PhoneDetailView(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)

    def get_object(self, id):
        try:
            return PhoneItems.objects.get(id=id)
        except PhoneItems.DoesNotExist as e:
            return Response( {"error": "Given question object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serailizer = PhoneItemsSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = PhoneItemsSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)

class ProductDetailView(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)

    def get_object(self, id):
        try:
            return SecondChoice.objects.get(id=id)
        except SecondChoice.DoesNotExist as e:
            return Response( {"error": "Given question object not found."}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serailizer = SecondChoiceSerializer(instance)
        return Response(serailizer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = SecondChoiceSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return HttpResponse(status=204)



