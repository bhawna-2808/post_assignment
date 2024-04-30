$(document).on("click", "#login_button", function (e) {
    e.preventDefault();
    alert("dd")
    var url = $(this).data("url");
    var email = $('#email').val()
    var password = $('#password').val()
    $.ajax({
        url: url,
        type: 'Post',
        data: {'email':email,'password':password, 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        dataType: 'json',
        beforeSend: function() {
        },
        success: function(data) {
        if (data.status === 'success') {
            $('#messages').html("Login successfully.");
            $('#messages').show();
            setTimeout(function() {
                window.location.href = '/dashboard';  // Replace '/dashboard/' with the URL you want to redirect to
            }, 1000);  // 1000 milliseconds = 1 second
        } else {
            $('#message').html("Invalid email and password.");
            $('#message').show();

        }

        }
    });
    

})