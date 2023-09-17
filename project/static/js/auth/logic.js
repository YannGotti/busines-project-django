

function showRegister(){
    let login = document.getElementById('login');
    login.style.display = 'none';

    let navbarNav = document.getElementById('navbarNav');
    navbarNav.style.display = 'none';

    let register = document.getElementById('register');
    register.style.display = 'block';

}

function showLogin(){
    let login = document.getElementById('login');
    login.style.display = 'block';

    let navbarNav = document.getElementById('navbarNav');
    navbarNav.style.display = 'block';

    let register = document.getElementById('register');
    register.style.display = 'none';
}

function selectTypeUser(type){
    let type_user = document.getElementById('type_user');
    type_user.textContent = type.textContent;
}