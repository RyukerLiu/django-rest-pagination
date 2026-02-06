from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', include(router.urls)),
]
