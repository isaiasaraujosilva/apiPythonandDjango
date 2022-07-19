from atexit import register
from django.contrib import admin
from django.db import router
from django.urls import path,include
from api.views import ClienteViewSet, ProdutoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'produto', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
