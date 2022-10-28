from django.urls import path


from .views import transformer_list

urlpatterns = [
    path('', transformer_list, name='file-upload'), 

]
