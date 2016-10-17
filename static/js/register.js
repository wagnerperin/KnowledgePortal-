function addUser(event) {
    event.preventDefault();

    var formData = {
        first_name: $('#first_name').val(),
        last_name: $('#last_name').val(),
        email: $('#email').val(),
        username: $('#name').val(),
        password: $('#word').val(),
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: 'http://localhost:8000/register/',
        contentType: 'application/x-www-form-urlencoded',
        dataType: 'text',
        data: formData,
    }).done(function(data) {
        console.log('Success:', data);
    }).fail(function(data) {
        console.log('Errooooouuu!', data);
    });
}
