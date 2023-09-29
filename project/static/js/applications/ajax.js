
function RefusalApplication(id, recipient){
    let csrftoken = getCookie('csrftoken');

    let data = 
    {
        id: id,
        recipient_id: recipient
    }
    
    $.ajax({
        url: '/application/refusalApplication/',
        method: 'post',
        data: data,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data){
            if (data == 'ok'){
                location.reload()
            }
            else {
                console.error('Ошибка аунтефикации!');
            }
        },
        error: function (jqXHR, exception) {
            return;
        }
    });
}


function SubmitApplication(id, recipient){
    let csrftoken = getCookie('csrftoken');

    let data = 
    {
        id: id,
        recipient_id: recipient
    }
    
    $.ajax({
        url: '/application/submitApplication/',
        method: 'post',
        data: data,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data){
            if (data == 'ok'){
                location.reload()
            }
            else {
                console.error('Ошибка аунтефикации!');
            }
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