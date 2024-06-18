from common.constants import ChoicesEnum


class PaymentStatus(ChoicesEnum):
    PENDING = 'pending'
    COMPLETED = 'completed'
    FAILED = 'failed'

