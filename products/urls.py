from django.urls import path
from .views import ProductFormView

urlpatterns = [
    path("", ProductFormView.as_view(), name="products:list"),
    path("add", ProductFormView.as_view(), name="products:add"),
]
