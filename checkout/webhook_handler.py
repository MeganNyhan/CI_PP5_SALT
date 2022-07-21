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
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )
