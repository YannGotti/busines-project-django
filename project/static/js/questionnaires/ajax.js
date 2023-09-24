

function SubmitFilter(type){

    $.ajax({
        url: '/questionnaires/filter?filter=' + type.textContent,
        method: 'get',
        success: function(data){
            fillQuestionnairesCards(data);
        },
        error: function (jqXHR, exception) {
            return;
        }
    });
}

function fillQuestionnairesCards(data){
    let questionnaires_cards = document.getElementById('questionnaires_cards');
    questionnaires_cards.innerHTML = ``;

    let isWorking = data.type_user == 'Предприниматель';

    for (const card of data.data) {
        questionnaires_cards.innerHTML += 
        `
        <div class="col-12 col-md-6 col-lg-4">

            <div class="card bg-dark">
                <div class="card-body">
                  <h5 class="card-title text-h4-custom">`+ card.new_work +`</h5>
                  <p class="card-text text-h5-custom">`+ card.areaOfWork +`</p>
                  <p class="card-text text-h5-custom">Желаемая зарплата: `+ card.salary +` RUB</p>
                  <p class="card-text text-h5-custom">Есть ли опыт работы: `+ card.experience +`</p>
                    
                  <div class="row" id='isWorking_' `+ card.id +`>


                    <div class="col-6">
                        <a href="/@id`+ card.user_id +`/" class="btn btn-light text-h5-custom text-dark">Посмотреть профиль</a>
                    </div>

                  </div>
                  
                </div>
            </div>
            
        </div>
        `;


        if (isWorking){
            let isWorking = document.getElementById('isWorking_' + card.id);
            isWorking.innerHTML += 
            `
            <div class="col-6">
                <a href="#" class="btn btn-outline-light text-h5-custom">Предложить сотрудничество</a>
            </div>
            `;
        }

    }



}

