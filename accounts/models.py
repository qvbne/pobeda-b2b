from django.db import models
from django.contrib.auth.models import User


class CompanyProfile(models.Model):

    ROLE_CHOICES = (
        ('consumer', 'Потребитель'),
        ('producer', 'Производитель'),
        ('admin', 'Администратор'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(
        max_length=255,
        blank=True,
        default=''
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='consumer'
    )

    def __str__(self):
        return self.company_name