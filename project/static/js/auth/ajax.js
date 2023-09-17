

function registerUser(){
    let csrftoken = getCookie('csrftoken');
    let field_validation = document.getElementById("field_validation");
    let form = document.forms.register_form;

    let password = form.elements.password;
    let submit_password = form.elements.submit_password;
    let fullName = form.elements.fullName;
    let email = form.elements.email;
    let userPlaceOfStudy = form.elements.userPlaceOfStudy;
    let type_user = document.getElementById('type_user').textContent;

    if (password.value != submit_password.value){
        field_validation.innerText = `Пароли не совпадают`;
        return;
    }

    if (password.value.length <=6 || password.value.length >= 30){
        field_validation.innerText = `Пароль не может быть меньше 6 символов или больше 30.`;
        return;
    }

    if (submit_password.value.length <=6 || submit_password.value.length >= 30){
        field_validation.innerText = `Пароль не может быть меньше 6 символов или больше 30.`;
        return;
    }

    if (fullName.value.length <=3 || fullName.value.length >= 25){
        field_validation.innerText = `Имя пользователя не может быть меньше 3 символов и больше 25.`;
        return;
    }

    if (!email.value.includes('@')){
        field_validation.innerText = `Почта должна содержать символ @`;
        return;
    }

    field_validation.innerText =``;

    let userData = 
    {
        fullName : fullName.value,
        password: password.value,
        email: email.value,
        userPlaceOfStudy: userPlaceOfStudy.value,
        type_user : type_user
    }
    
    $.ajax({
        url: '/auth/register/',
        method: 'post',
        data: userData,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data){
            if (data == "Not"){
                field_validation.innerText = `Пользователь с такой почтой уже существует!`;
                return;
            }

            if (data == 'Ok'){
                ShowValidateAccount();
            }
        },
        error: function (jqXHR, exception) {
            return;
        }
    });
}

function ShowValidateAccount(){
    let validateAccount = document.getElementById('validateAccount');
    validateAccount.style.display = 'block';

    let register = document.getElementById('register');
    register.style.display = 'none';

    let login = document.getElementById('login');
    login.style.display = 'block';
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}