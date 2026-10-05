from django.urls import path
from .views import *

urlpatterns = [

    path('customers',customerpage),
    path('productdetails',prodectdetailpage)
]