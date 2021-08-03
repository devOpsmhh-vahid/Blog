from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from users.api.serializers import (UserSerializer)
from users.models import (User)

# from django.contrib.auth.models import User



class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetailView(RetrieveUpdateDestroyAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer



