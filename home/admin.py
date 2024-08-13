from django.contrib import admin
from .models import Product

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'status')

# admin.site.register(Product, ProductAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'status')
    list_filter = ('id', 'name', 'status')
    list_editable = ('name', 'price')
    list_per_page = 25