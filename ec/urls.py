from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello/v<int:version>/', views.hello_version, name='hello-version'),
    path('', include(router.urls)),
]
