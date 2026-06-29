from django import core # validasyon için
from django import forms
from .models import product


class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['İsim','Fiyat','Açıklama','Resim']


    def clean_price(self):
        price = self.cleaned_data.get('price')


        if price is not None and price <=0:
            raise forms.ValidationError("Bir ürünün fiyatı eksi veya 0 olamaz")
        

        return price