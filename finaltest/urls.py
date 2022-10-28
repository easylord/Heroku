from django.urls import path
from .views import  PollViewSet, AlbumViewSet

urlpatterns = [
    path('final/', PollViewSet.as_view({"get": "list", "post": "create"}), name='poll_addd'),
    path('album/', AlbumViewSet.as_view({"get": "list", "post": "create"}), name='poll_addd'),




    


]
