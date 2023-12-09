from .views import *
from django.urls import path


urlpatterns = [
    path('', CategoryApiView.as_view())
]
