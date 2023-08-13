from rest_framework import serializers
from .models import MenuItem, Category

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']

#class MenuItemSerializer(serializers.ModelSerializer):
    
    from django.contrib.auth.models import User 
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = User 
        fields = ['url', 'username', 'email', 'groups']