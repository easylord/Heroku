from django.urls import path


from .views import transformer_detail, transformer_list

urlpatterns = [
    path('', transformer_list, name='file-upload'), 
    path('<int:pk>', transformer_detail, name='file-upload'), 

]
