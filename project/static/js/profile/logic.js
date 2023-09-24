

function showQuestionnairePanel(){
    let questionnaire_panel = document.getElementById('questionnaire_panel');
    questionnaire_panel.style.display = 'none';

    let questionnaire_form_block = document.getElementById('questionnaire_form_block');
    questionnaire_form_block.style.display = 'block';
}

function showHideSalaryField(flexCheckDefault){
    let solary_field = document.getElementById('solary_field');
    if (flexCheckDefault.checked){
        solary_field.style.display = 'none';
    }
    else{
        solary_field.style.display = 'block';
    }
}


function selectAreaOfWork(type){
    let areaOfWork = document.getElementById('areaOfWork');
    areaOfWork.textContent = type.textContent;
}

function fillTypeProffesion(){
    let profession_list = document.getElementById('profession_list');
    for (let profession of listProffesion) {
        profession_list.innerHTML += `<li><a class="dropdown-item text-light bg-dark" href="#" onclick="selectAreaOfWork(this)">`+ profession + `</a></li>`
    }
}

fillTypeProffesion();



  