var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();


var style = {
    base: {
        color:'#806161',
        fontFamily:'Federo',
        fontSmootihing: 'antialised',
        fontSize: '16px',
        '::placeholder':{
            color:'rgba(128, 97, 97, 0.6)'
        }
    },
    invalid:{
        color:'#fa755a',
        iconColor: '#fa755a'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element')