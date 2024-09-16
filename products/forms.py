from django import forms

from products.models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label="Product Name", max_length=255)
    price = forms.FloatField(label="Product Price")
    description = forms.CharField(label="Product Description", widget=forms.Textarea)
    available = forms.BooleanField(
        label="Product Availability", initial=True, required=False
    )
    photo = forms.ImageField(label="Product Photo", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            price=self.cleaned_data["price"],
            description=self.cleaned_data["description"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
