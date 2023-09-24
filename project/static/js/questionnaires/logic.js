

function selectAreaOfWorkFilter(type){
    let areaOfWork = document.getElementById('areaOfWork');
    areaOfWork.value = type.textContent;
}

const searchInput = document.getElementById('areaOfWork');
const professionList = document.getElementById('profession_list');

searchInput.addEventListener('input', () => {
  const searchTerm = searchInput.value.toLowerCase();
  professionList.innerHTML = '';

  for (let i = 0; i < listProffesion.length; i++) {
    const profession = listProffesion[i].toLowerCase();
    if (profession.includes(searchTerm)) {
        const listItem = document.createElement('li');

        listItem.innerHTML += `<a class="dropdown-item text-light bg-dark" href="#" onclick="selectAreaOfWorkFilter(this);SubmitFilter(this)">`+ listProffesion[i] + `</a>`
        
        professionList.appendChild(listItem);
    }
  }
});

