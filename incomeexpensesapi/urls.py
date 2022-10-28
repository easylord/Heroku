"""incomeexpensesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from things.views import Studentapi, Marksapi
from subCategory.views import FinalLinkViewsets , LaptopItems


schema_view = get_schema_view(
    openapi.Info(
        title="INCOME EXPENSES API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register("Studentmodel", Studentapi)
router.register("Marksmodel", Marksapi)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    #path('api/', include('core.urls')),

    path('social_auth/', include(('social_auth.urls', 'social_auth'),
                                 namespace="social_auth")),
    path('expenses/', include('expenses.urls')),
    path('income/', include('income.urls')),
    path('products/', include('product.urls')),

    path('userstats/', include('userstat.urls')),
    path('things/', include(router.urls,)),
    path('multiple/', include('things.urls')),
    path('reviews/', include('Reviews.urls')),
    path('stores/', include('stores.urls')),
    path('test/', include('test.urls')),
    path('add/', include('things.urls')),
    path('final/', include('finaltest.urls')),
    path('cart/', include('cart.urls')),






    path('categories/', include('category.urls')),
    path('imagebanner/', include('banner.urls')),

    path('subCategories/', include('subCategory.urls')),



    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]


handler404='utils.views.error_404'
handler500='utils.views.error_500'

