from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from users.models import (User)


class UserSerializer(ModelSerializer):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        model = User
        fields = "__all__"

