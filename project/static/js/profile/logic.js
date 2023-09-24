

function showQuestionnairePanel(){
    let questionnaire_panel = document.getElementById('questionnaire_panel');
    questionnaire_panel.style.display = 'none';

    let questionnaire_form_block = document.getElementById('questionnaire_form_block');
    questionnaire_form_block.style.display = 'block';
}

function showProjectPanel(){
    try {
        let project_panel = document.getElementById('project_panel');
        project_panel.style.display = 'none';
    } catch (error) {
        
    }
    

    let project_form_block = document.getElementById('project_form_block');
    project_form_block.style.display = 'block';
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

function addFieldPostInput(element){
    let postProjectGrid = document.getElementById('postProjectGrid');

    if (element.parentNode != postProjectGrid.lastElementChild){
        return;
    }

    postProjectGrid.insertAdjacentHTML('beforeend', 
        `
        <div class="col-12 col-md-12 col-lg-6">
            <input type="text" name="postProject" placeholder="web designer" class="form-control input_post m-2" onfocus="addFieldPostInput(this)" onblur="delFieldPostInput(this)">
        </div>
        `
    );

}

function delFieldPostInput(element){
    let postProjectGrid = document.getElementById('postProjectGrid');

    if ((element.value == '' || element.value == null) && (postProjectGrid.lastElementChild.children[0].value == '' || postProjectGrid.lastElementChild.children[0].value == null)){
        postProjectGrid.lastElementChild.remove();
    }
}







  