from rest_framework import serializers

from .models import User, Content

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name')

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id','name','author')
