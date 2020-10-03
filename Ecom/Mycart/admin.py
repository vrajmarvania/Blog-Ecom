from django.contrib import admin

from .models import Product,Contect,Order,Orderupdate
admin.site.register(Product)

admin.site.register(Contect)
admin.site.register(Order)
admin.site.register(Orderupdate)