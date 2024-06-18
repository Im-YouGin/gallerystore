from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_409_CONFLICT

from payments.connector import JCCGatewayPaymentsConnector
from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentCreateView(GenericAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request):
        payment = self.__create_payment(request)
        gateway_response = self.__register_payment_request(payment)

        if error_msg := gateway_response.get('errorMessage'):
            return JsonResponse({'error': error_msg}, status=HTTP_409_CONFLICT)

        return JsonResponse({'form_url': gateway_response['formUrl']}, status=HTTP_201_CREATED)

    def __create_payment(self, request) -> Payment:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    @staticmethod
    def __register_payment_request(payment: Payment) -> dict:
        return JCCGatewayPaymentsConnector().register_payment(payment.amount, payment.currency, payment.order_id)



