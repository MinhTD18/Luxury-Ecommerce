from django.db import models

from common.common_models import TimeStampMixin
from django.contrib.auth.models import User


class ShippingAddress(TimeStampMixin):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address