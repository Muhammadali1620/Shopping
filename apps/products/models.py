from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    category = models.ForeignKey('categories.Category', on_delete=models.PROTECT, related_name='products')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    desc = models.TextField(max_length=1500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.price}'
    
    def get_first_image(self):
        return self.images.first().image.url if self.images.exists() else None


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='%Y/%m/%d')

