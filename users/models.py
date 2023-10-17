from django.contrib.auth.models import AbstractUser
from django.db import models

from pages.models import Department, ConsumerCategory


class CustomUser(AbstractUser):
    consumer_category = models.ForeignKey(ConsumerCategory, on_delete=models.CASCADE, blank=True, null=True)
    users_department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)

