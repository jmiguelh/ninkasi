from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from empresas.views import EmpresaViewSet

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
