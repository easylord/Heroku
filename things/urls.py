from django.urls import path
from .views import Studentapi, SearchFilterView, create_products ,PollViewSet

urlpatterns = [
    path('', Studentapi, name='things'),
    path('try/', SearchFilterView.as_view(), name="Itemsub" ),
    path('create/', create_products, name='create-products'),
    path('addition/', PollViewSet.as_view({"get": "list", "post": "create"}), name='poll_addd'),



    


]
