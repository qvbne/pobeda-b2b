from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    unit = models.CharField(
        max_length=20,
        default='кг'
    )

    price_per_unit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    min_order_quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1
    )

    available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name