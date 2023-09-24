let recipient = 0
let sender = 0

function SetRecipient(rec){
    recipient = rec
}

function SetSender(sen){
    sender = sen
}

function ShowModal(){
    let modal_application_div = document.getElementById('modal_application_div');

    modal_application_div.innerHTML +=
    `
    <div class="modal" tabindex="-1" class="modal" id="exampleModalCenter" tabindex="-1" aria-labelledby="exampleModalCenterTitle" aria-modal="true" role="dialog">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content bg-dark">
        <div class="modal-header d-flex justify-content-center">
          <div class="col-4">
            <h5 class="modal-title text-h4-custom">ОТПРАВКА ЗАЯВКИ</h5>
            </div>
        <div data-bs-theme="dark">
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        </div>
        <div class="modal-body">

            <div class="row d-flex justify-content-center mt-3">
                <div class="col-12 col-lg-9">
                    <form name="application_form" id="application_form">

                        <div class="form-outline mb-3 " style="width: 100%; max-width: 22rem">
                            <label for="exampleInputEmail1" class="form-label text-h4-custom">РАССКАЖИТЕ О СЕБЕ, ПОЧЕМУ ВЫБРАЛИ ДАННОГО СОИСКАТЕЛЯ ИЛИ ПРОЕКТ</label>
                            <textarea type="text" name="message" class="form-control text-h5-custom" rows="4"></textarea>
                        </div>
        
                        <div class="form-outline mb-3" style="width: 100%; max-width: 22rem">
                            <label for="exampleInputEmail1" class="form-label text-h4-custom">НОМЕР ТЕЛЕФОНА ДЛЯ СВЯЗИ</label>
                            <input type="text" name="number_phone" id="phone" class="form-control custom-number_phone text-h5-custom" placeholder="7 (XXX) XXX-XXXX"/>
                        </div>

                        <h3 class="text-h6-custom text-center text-danger mt-3" id="field_validation"></h3>
                        
                    </form>
                    
                </div>

            </div>

        </div>
        <div class="modal-footer d-flex justify-content-center">
            <div class="col-6 text-center">
                <button type="button" class="btn btn-outline-light content-text-custom button2-animation mt-2 mb-2" onclick="SendApplication()" >ОТПРАВИТЬ</button>
            </div>
        </div>
      </div>
    </div>
</div>
    `;
}

ShowModal();


function SendApplication(){
    let csrftoken = getCookie('csrftoken');
    let field_validation = document.getElementById("field_validation");
    let form = document.forms.application_form;

    let message = form.elements.message;
    let number_phone = form.elements.number_phone;
    
    if (message.value.length >= 200){
        field_validation.innerText = `Поля не могут иметь размер более 200 символов`;
        return;
    }

    if (number_phone.value.length >= 20 || number_phone.value.length <= 8){
        field_validation.innerText = `Поля не могут иметь размер более 200 символов или меньше 8`;
        return;
    }


    field_validation.innerText =``;

    let Data = 
    {
        message : message.value,
        number_phone : number_phone.value,
        recipient_id : recipient,
        sender_id : sender
    }

    $.ajax({
        url: '/application/sendApplication/',
        method: 'post',
        data: Data,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(data){
            //location.reload();
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