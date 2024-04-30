$(document).on("click", "#submitt_btnn", function (e) {
  e.preventDefault();
  var url = $(this).data("url");
  var first_name = $('#first_name').val()
  var last_name = $('#last_name').val()
  var email = $('#email').val()
  var password = $('#password').val()
  var mobile_no = $('#mobile_number').val()
  var error = 0
  if (first_name === "") {
    $('.first_name_error').html("This field is required");
    error++;
    } else {
    $('.first_name_error').html("");
    }
    if (last_name === "") {
        $('.last_name_error').html("This field is required");
        error++;
        } else {
        $('.last_name_error').html("");
        }
    if (email === "") {
        $('.email_error').html("This field is required");
        error++;
        }
        else {
        $('.email_error').html("");
    }
    if (password === "") {
    $('.password_error').html("This field is required");
    error++;
    } else {
    $('.password_error').html("");
    }
    if (mobile_no === "") {
    $('.mob_error').html("This field is required");
    error++;
    } else {
    $('.mob_error').html("");
    }

    if (error != 0) {
        return false; 
      }
    else {
    $.ajax({
        url: url,
        type: 'Post',
        data: {'first_name':first_name,'last_name':last_name, 'email':email,'password':password, 'mobile_no':mobile_no, 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
        dataType: 'json',
        beforeSend: function() {
        },
        success: function(data) {
        if (data.status === 'success') {
            $('#messages').html("User registered successfully.");
            $('#messages').show();
            $('#first_name').val('');
            $('#last_name').val('');
            $('#email').val('');
            $('#password').val('');
            $('#mobile_number').val('');
        } else {
            // User registration failed
            alert('An error occurred while registering user. Please try again.');
        }

        }
    });
    }   
})