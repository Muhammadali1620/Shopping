from django.contrib import admin

from apps.products.models import Product, ProductImage


class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    min_num = 1
    max_num = 10
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale_price', 'desc',)
    prepopulated_fields = {'slug': ['title']}
    readonly_fields = ('created_at',)
    inlines = [ProductImageInlineAdmin, ]
    list_display_links = list_display
    search_fields = ('title', 'price')
