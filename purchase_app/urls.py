from .views import *
from django.urls import path


urlpatterns = [
    path('info/', PurchaseApiView.as_view()),
]
