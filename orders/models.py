from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Order(models.Model):

    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('confirmed', 'Подтвержден'),
        ('in_progress', 'В производстве'),
        ('ready', 'Готов'),
        ('completed', 'Выполнен'),
        ('cancelled', 'Отменён'),
    )

    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    order_number = models.CharField(
        max_length=50,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    comment = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def save(self, *args, **kwargs):

        self.total_price = (
            self.quantity * self.unit_price
        )

        super().save(*args, **kwargs)