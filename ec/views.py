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
                {"id": 1, "text": "hello"},
                {"id": 2, "text": "hi"},
                {"id": 3, "text": "bonjour"},
                {"id": 4, "text": "hola"},
            ],
        }
    )
