function uploadPhotoProfile(id, image){
    let csrftoken = getCookie('csrftoken');

    let formData = new FormData();
    formData.append('id', id);
    formData.append('file', image.files[0]);

    $.ajax({
        url: '/profile/uploadPhoto/',
        method: 'post',
        data: formData,
        async: false,
        cache: false,
        contentType: false,
        enctype: 'multipart/form-data',
        processData: false,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data){
            location.reload();
        },
        error: function (jqXHR, exception) {
            return;
        }
    });
}


function sendQuestionnaire(user_id){
    let csrftoken = getCookie('csrftoken');
    let field_validation = document.getElementById("field_validation");
    let form = document.forms.questionnaire_form;

    let new_work = form.elements.new_work;
    let areaOfWork = form.elements.areaOfWork;
    let old_work = form.elements.old_work;
    let experience = form.elements.experience;
    let salary = form.elements.salary;
    let freework = form.elements.freework;
    let id = user_id;

    if (new_work.value.length >= 200){
        field_validation.innerText = `Поля не могут иметь размер более 200 символов`;
        return;
    }

    if (areaOfWork.value.length >= 200){
        field_validation.innerText = `Поля не могут иметь размер более 200 символов`;
        return;
    }

    if (old_work.value.length >= 200){
        field_validation.innerText = `Поля не могут иметь размер более 200 символов`;
        return;
    }

    if (experience.value.length >= 200){
        field_validation.innerText = `Поля не могут иметь размер более 200 символов`;
        return;
    }

    if (!isNumeric(salary.value)) {
        field_validation.innerText = "Пожалуйста, введите только числа в поле желаемой зарплаты.";
        return;
    }

    field_validation.innerText =``;

    let Data = 
    {
        new_work : new_work.value,
        areaOfWork: areaOfWork.value,
        old_work: old_work.value,
        experience: experience.value,
        salary : salary.value,
        freework: freework.checked,
        id : id
    }

    $.ajax({
        url: '/profile/sendQuestionnaire/',
        method: 'post',
        data: Data,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data){
            console.log(data)
        },
        error: function (jqXHR, exception) {
            return;
        }
    });
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


function isNumeric(value) {
    return /^-?\d+$/.test(value);
}