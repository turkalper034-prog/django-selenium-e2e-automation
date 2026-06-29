from django.contrib import admin
from django.urls import path,include
from products.views import index, product_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('',index,name='Home'),
    path('delete/<int:product_id>/', product_delete, name='product_delete'),
]
