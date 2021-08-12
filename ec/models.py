from django.db import models


class Order(models.Model):
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
