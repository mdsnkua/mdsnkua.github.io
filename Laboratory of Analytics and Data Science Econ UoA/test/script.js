// script.js
function flip(element) {
  element.querySelector('.front').style.transform = 'rotateY(180deg)';
  element.querySelector('.back').style.transform = 'rotateY(360deg)';
}

function flipBack(element) {
  element.querySelector('.front').style.transform = 'rotateY(0deg)';
  element.querySelector('.back').style.transform = 'rotateY(180deg)';
}
