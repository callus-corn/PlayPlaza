from rest_framework import routers
from .views import UserViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contents', ContentViewSet)
