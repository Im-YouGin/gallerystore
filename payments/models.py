import uuid

from django.db import models

from common.database import TimestampedModel
from payments.constants import PaymentStatus


class Payment(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_id = models.CharField(max_length=36)
    status = models.CharField(max_length=20, choices=PaymentStatus.choices(), default=PaymentStatus.PENDING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} - Status {self.status}"
