function login(event) {
    event.preventDefault();
    var username = $('#username').val();
    var password = $('#password').val();

    var formData = {
        client_id: 'KAivTIRh7e1ojpEGPh37rV5o3VDwDjeqjsIBMwE2',
        client_secret: 'mCZ27ZvCCK3lAQv06OpehN8WSwT8YWJAZ8I3XZmrxFygMh8qvPcMCNaK5YbiIP5GKntNIyKDU9cx0GXMH2arOjMLeGpdhMQaMvwxWti7t6nu8HKpcBg4pi8JxcbCQ2Iu',
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
        localStorage.setItem("access_token", data['access_token']);
        localStorage.setItem("token_type", data['token_type']);
        localStorage.setItem("expires_in", data['expires_in']);
        localStorage.setItem("refresh_token", data['refresh_token']);
        localStorage.setItem("scope", data['scope']);
    }).fail(function(data) {
        toastr.error('Login Falhou!');
        console.log('Errooooouuu!', data);
    });;
}

function logout() {
    localStorage.clear();
}
