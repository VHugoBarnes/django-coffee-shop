from django.urls import path
from .views import ProductFormView, ProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("add", ProductFormView.as_view(), name="products_add"),
]
