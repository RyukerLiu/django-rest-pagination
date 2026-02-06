from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(["GET"])
def hello(request):
    return Response(
        {
            "message": "hello",
            "versions": [
                {"version": 1, "path": "/hello/v1/"},
                {"version": 2, "path": "/hello/v2/"},
                {"version": 3, "path": "/hello/v3/"},
                {"version": 4, "path": "/hello/v4/"},
            ],
        }
    )


@api_view(["GET"])
def hello_version(request, version):
    if version not in {1, 2, 3, 4}:
        return Response({"detail": "Not found."}, status=404)
    return Response({"message": "hello", "version": version})
