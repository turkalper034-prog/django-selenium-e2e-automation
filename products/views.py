from django.db.models import Q
from django.shortcuts import redirect, render
from .models import product
from .forms import productForm
from django.contrib import messages

def index(request):
    

    if request.method == "POST":

        form = productForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Ürün Başarıyla Kaydedildi!")
            return redirect('Home')


    else:
        form = productForm

    search_words = request.GET.get('q', '').strip()

    if search_words:
        # Eğer kullanıcı arama kutusuna sadece SAYI girdiyse (Örn: 13000)
        if search_words.isdigit():
            products = product.objects.filter(Fiyat=int(search_words)).order_by("-Fiyat")

        # Eğer kullanıcı HARF girdiyse (Örn: Sonny veya Yapay Zeka)
        else:
            products = product.objects.filter(
                İsim__icontains=search_words
            ).order_by("-Fiyat")

            # Eğer isimde bulamazsa, bir de açıklamada aramayı dene
            if not products.exists():
                products = product.objects.filter(
                    Açıklama__icontains=search_words
                ).order_by("-Fiyat")
    else:
        # Arama kutusu boşsa tüm ürünleri getir
        products = product.objects.all().order_by("-Fiyat")

    context = {
    "products": products,
    "query": search_words,
    "form": form
}

    return render(request, 'index.html', context)


def product_delete(request, product_id):
    urun = product.objects.get(id=product_id)
    urun.delete()
    messages.warning(request,"Ürün Başarıyla Silindi.")

    return redirect('Home')