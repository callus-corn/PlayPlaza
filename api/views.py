import django_filters
from rest_framework import viewsets, filters, permissions

from .models import User, Content
from .serializer import UserSerializer, ContentSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

