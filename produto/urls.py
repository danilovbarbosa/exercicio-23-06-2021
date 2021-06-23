from django.urls import path, include

from rest_framework import routers

from produto import views

router = routers.DefaultRouter()
router.register(r"produto", views.ProdutoViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
