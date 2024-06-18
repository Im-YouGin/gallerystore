from django.urls import path

from payments.views import PaymentCreateView

urlpatterns = [
    path('payments/', PaymentCreateView.as_view(), name='create_payment'),
]

