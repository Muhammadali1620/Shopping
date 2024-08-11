from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}: {self.product}'
