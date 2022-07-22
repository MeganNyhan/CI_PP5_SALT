from django.http import HttpResponse


class StripeWH_Handler:
    """
        Handles Stripe Webhook
    """
    def __int__(self, request):
        self.request = request

    def handle_event(self, event):
        """
            Handle generic/ or unkown webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
            Handle the payment_intent.succedded webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
            Handle the payment_intent_payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )