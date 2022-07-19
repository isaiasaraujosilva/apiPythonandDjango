from atexit import register
from django.contrib import admin
from django.db import router
from django.urls import path,include
from api.views import ClienteViewSet, ProdutoViewSet, PedidoViewSet, faturamentoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'pedido', PedidoViewSet,basename='pedido')
router.register(r'pedido/(?P<cliente>[id])', PedidoViewSet,basename='pedido')
router.register(r'faturamento', faturamentoViewSet)


#router.register(r'pedido/cliente', PedidoPorClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
