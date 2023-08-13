from django.urls import path
from . import views

urlpatterns = [
    # path('category', views.CategoriesView.as_view()),
    # path('menu-items', views.MenuItemsView.as_view()),
]

from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    . . . ,
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
path('auth/', include('djoser.urls')),
path('auth/', include('djoser.urls.authtoken')),
path('api-token-auth/', obtain_auth_token)
]


#add following lines to update urlpatterns list
