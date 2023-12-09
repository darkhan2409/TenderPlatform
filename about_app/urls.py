from .views import *
from django.urls import path


urlpatterns = [
    path('', CompanyApiView.as_view()),
    path('update/<int:about_id>/', CompanyUpdateApiView.as_view())
]
