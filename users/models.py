from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,

    )
    GENDER = (
        (1,'Male'),
        (2,'Femail'),

    )
    gender = models.SmallIntegerField(
        null=False,
        blank=False,
        default=1,
        choices=GENDER
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    def __str__(self) -> str:
        return self.username