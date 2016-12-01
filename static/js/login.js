function login(event) {
    event.preventDefault();
    var username = $('#username').val();
    var password = $('#password').val();

    var formData = {
        client_id: 'uE5EuXg',
        grant_type: 'password',
        username: username,
        password: password,
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
        url: 'http://localhost:8000/o/token/',
        contentType: 'application/x-www-form-urlencoded',
        data: formData,
    }).done(function(data) {
        console.log('Success:', data);

        data['username'] = username;
        post('/login', data);
    }).fail(function(data) {
        toastr.error('Login Falhou!');
        console.log('Errooooouuu!', data);
    });;
}

function logout() {
    localStorage.clear();
}

// Post to the provided URL with the specified parameters.
function post(path, parameters) {
    var form = $('<form></form>');

    form.attr("method", "post");
    form.attr("action", path);

    $.each(parameters, function(key, value) {
        var field = $('<input></input>');

        field.attr("type", "hidden");
        field.attr("name", key);
        field.attr("value", value);

        form.append(field);
    });
    var csrftoken = getCookie('csrftoken');

    field = $('<input></input>');
    field.attr("type", "hidden");
    field.attr("name", "csrfmiddlewaretoken");
    field.attr("value", csrftoken);
    form.append(field);

    // The form needs to be a part of the document in
    // order for us to be able to submit it.
    $(document.body).append(form);
    form.submit();
}
