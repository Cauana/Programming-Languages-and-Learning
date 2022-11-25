const turnon = document.getElementById('turnon');
const turnoff = document.getElementById('turnoff');
const lamp = document.getElementById('lamp');

turnon.addEventListener('click', lampon)
function islampbroken() {
    return lamp.src.indexOf('quebrada') > -1
}
function lampon() {
    if ( !islampbroken()){
    lamp.src = './img/ligada.jpg';
    }
}
function lampoff() {
    if (!islampbroken()){
    lamp.src = './img/desligada.jpg';
    }
}
function lampBroken() {
    lamp.src = './img/quebrada.jpg';
}


turnon.addEventListener('click', lampon);
turnoff.addEventListener('click', lampoff);
lamp.addEventListener('mouseover', lampon);
lamp.addEventListener('mouseleave', lampoff);
lamp.addEventListener('dblclick', lampBroken);