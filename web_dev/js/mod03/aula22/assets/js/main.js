const divParagrafos = document.querySelector('.div-paragrafos');
const paragrafos = divParagrafos.querySelectorAll('p');


const estilosBody = getComputedStyle(document.body);
const bodyBackgroundColor = estilosBody.backgroundColor;


for (let paragrafo of paragrafos) {
    paragrafo.style.backgroundColor = bodyBackgroundColor;
    paragrafo.style.color = 'blue';
}