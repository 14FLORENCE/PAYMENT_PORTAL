// make_payment.js

$(document).ready(function() {
    $('#payment_method').on('change', function() {
        var selectedMethod = $(this).val();
        // Example: show additional fields for credit card if card is selected
        if (selectedMethod === 'card') {
            // Insert custom logic for card payment
            alert("You selected Credit/Debit Card as your payment method.");
        }
    });
});
