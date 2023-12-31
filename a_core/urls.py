"""
URL configuration for a_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

SchemaView = get_schema_view(
    info=openapi.Info(
        title='TenderPlatform',
        default_version='v1.0',
        description='Special tender platform for suppliers',
        terms_of_service='',
        contact=openapi.Contact(name='Darkhan Seilbekov'),
        license=openapi.License(name='JustCode')
    ),
    patterns=[
        path('supplier/', include('supplier_app.urls')),
        path('status/', include('status_app.urls')),
        path('category/', include('category_app.urls')),
        path('about/', include('about_app.urls')),
        path('purchase/', include('purchase_app.urls')),
    ],
    public=True,
    permission_classes=[AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('supplier/', include('supplier_app.urls')),
    path('status/', include('status_app.urls')),
    path('category/', include('category_app.urls')),
    path('about/', include('about_app.urls')),
    path('purchase/', include('purchase_app.urls')),
    path('swagger/', SchemaView.with_ui()),
]
