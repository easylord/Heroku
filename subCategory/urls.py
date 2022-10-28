from django.urls import  path
from . import views


urlpatterns = [
    path('', views.subCategoryViewsets.as_view(), name='file-upload'),
    path('laptop/',views.LaptopStudentapi.as_view({"get": "list", "post": "create",}), name="laptop" ),
    path('itemssub/',views.ItemSubCategoryViewsets.as_view(), name="Itemsub" ),
    path('test/<product>',views.EventDetailView.as_view(), name="Itemsub" ),
    path('create/',views.showmultiplemodels, name="Itemsub" ),
    path('detail/<int:laptop_items>',views.ArticleDetailView.as_view(), name="Itemsub" ),
    #path('create/<product>/',views.TodoDetail.as_view(), name="Itemsub" ),
    path('create/<product>/',views.TodoDetailphone.as_view(), name="Itemsub" ),



]
