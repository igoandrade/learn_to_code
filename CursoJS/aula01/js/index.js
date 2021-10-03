const nomeCompleto = 'Igo da Costa Andrade';
const idade = 36;
const peso = 85;
const altura = 1.60;
let imc = peso / (altura * altura);

let conteudo = document.getElementById('conteudo');

conteudo.innerHTML += `<p>${nomeCompleto} tem ${idade} anos.</p>`;
conteudo.innerHTML += `<p>Sua altura é ${altura} m e seu peso ${peso} kg.</p>`;
conteudo.innerHTML += `<p>Seu índice de massa corporal é ${imc.toFixed(2)}.</p>`;