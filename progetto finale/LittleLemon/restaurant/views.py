# from rest_framework import generics
# from .models import MenuItem, Category
# from .serializers import MenuItemSerializer, CategorySerializer

# class CategoriesView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView): 
queryset = MenuItem.objects.all() 
serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):     
queryset = MenuItem.objects.all() 
serializer_class = MenuItemSerializer