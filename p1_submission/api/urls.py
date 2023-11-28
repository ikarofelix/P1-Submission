from django.contrib import admin
from django.urls import path, include
from api.views import ItemList, ItemDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
]

