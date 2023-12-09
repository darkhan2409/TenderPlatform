from .views import *
from django.urls import path


urlpatterns = [
    path('', StatusApiView.as_view())
]