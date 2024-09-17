$(document).ready(function() {
    // Handle Logout Button Click
    $("#logoutBtn").click(function() {
        if (confirm("Are you sure you want to log out?")) {
            window.location.href = "/logout"; // Replace with your logout URL
        }
    });

    // Handle form submission with data saving
    $("form").submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = {
            amount: $("#amount").val(),
            payment_method: $("#payment_method").val()
        };

        // Save data via AJAX request (dummy example)
        $.ajax({
            url: "/process_payment", // Replace with your process URL
            type: "POST",
            data: formData,
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val() // Include CSRF token
            },
            success: function(response) {
                alert("Payment Successful!");
                window.location.href = "/success"; // Redirect to success page
            },
            error: function() {
                alert("Payment failed. Please try again.");
            }
        });
    });

    // Input focus animations
    $(".form-control").on("focus", function() {
        $(this).addClass("focused");
    }).on("blur", function() {
        $(this).removeClass("focused");
    });
});
