/* Core payment logic flow comes from here: https://stripe.com/docs/payments/accept-a-payment.
CSS comes from here: https://stripe.com/docs/stripe-js */

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var card = elements.create('card');

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: 'black',
        iconColor: '#dc3545'
    }
};

card.mount('#card-element', {style:style});