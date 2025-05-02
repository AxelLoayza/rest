from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrendaViewSet

router = DefaultRouter()
router.register(r'prendas', PrendaViewSet)  # Define la ruta para acceder a la API

urlpatterns = [
    path('', include(router.urls)),  # Incluye las rutas generadas por el router
]
