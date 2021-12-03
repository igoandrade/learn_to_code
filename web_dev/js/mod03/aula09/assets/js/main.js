const form = document.getElementById('form');
form.addEventListener('submit', e => {
    e.preventDefault();
})


function calculaIMC (peso, altura) {
    return peso / altura**2;
}

function estabeleceCategoria(imc) {

    if (imc <18.5) {
        return "Abaixo do Peso Normal";
    } else if (imc < 25.0) {
        return "Peso Normal";
    } else if (imc < 30.0) {
        return "Sobrepeso";
    } else if (imc < 35.0) {
        return "Obesidade Tipo 1";
    } else if (imc < 40.0) {
        return "Obesidade Tipo 2";
    } else  {
        return "Obesidade Tipo 3";
    }
}

function validaDados(strQuery, limInf, limSup) {
    let x = Number(document.getElementById(strQuery).value);
    if (!Number.isFinite(x) || x <= limInf || x >= limSup) {
        return false;
    } else {
        return true;
    }
}

function imprimeResultado() {
    let resultado = document.getElementById('resultado');
    resultado.style.display = 'block';
    resultado.innerHTML = '';
    if (validaDados('peso', 0, 600) && validaDados('altura', 0, 3.0)) {
        let peso = document.getElementById('peso').value;
        let altura = document.getElementById('altura').value; 
        let imc = calculaIMC(peso, altura);
        let categoria = estabeleceCategoria(imc);
        resultado.style.backgroundColor = "Aquamarine";
        resultado.innerHTML += `<h3>Resultado</</h3>`;
        resultado.innerHTML += `<p>Peso: ${peso} kg</p>`;
        resultado.innerHTML += `<p>Altura: ${altura} m</p>`;
        resultado.innerHTML += `<p>Seu IMC é ${imc.toFixed(2)} (<strong>${categoria}</strong>)</p>`;
        return;
    }
    resultado.style.backgroundColor = "Salmon";
    if (!validaDados('peso', 0, 300)) {
        resultado.innerHTML += "<p>Peso inválido!!</p>";
    }
    if (!validaDados('altura', 0, 2.5)) {
        resultado.innerHTML += "<p>Altura inválida!!</p>";
    }
    
}
