from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import BLANK_CHOICE_DASH
from rest_framework import serializers
# from django.contrib.auth.models import User
from users.models import (User)
# Create your models here.
import datetime

class PostModel(models.Model):
    title = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )
    txt = models.TextField(
        null=True,
        blank=True,
        max_length=500,
    )
    img = models.ImageField(
        null=True
    )
    like = models.IntegerField(
        default=0,
        null=True,
        blank=True, 

    )
    POST_TYPE = (
        (1,'post'),
        (2, 'repost')
    )
    post_type = models.CharField(
        max_length=20,
        default=1,
        choices=POST_TYPE,
    )
    parent = models.ForeignKey(
        blank=True,
        null=True,
        to='self',
        on_delete=models.CASCADE,

    )
    user = models.ForeignKey(
        null=True,
        blank=True,
        to=User,
        on_delete=models.CASCADE,
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    def __str__(self) -> str:
        if self.title == None:
            return "this is a repost"
        return self.title