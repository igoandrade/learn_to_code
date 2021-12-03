const elementos = [
    {tag: 'p', texto: 'Lorem ipsum dolor sit amet.'},
    {tag: 'div', texto: 'Ut enim ad minim veniam.'},
    {tag: 'section', texto: 'Et harum quidem rerum facilis.'},
    {tag: 'footer', texto: 'Excepteur sint occaecat cupidatat.'}
]


let container = document.querySelector('.container');
for (let i = 0; i < elementos.length; i++) {
    let {tag, texto} = elementos[i];
    let elemento = document.createElement(tag);
    let conteudo = document.createTextNode(texto);
    elemento.appendChild(conteudo);
    container.appendChild(elemento);
}

