function calcularMdc() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const resultado = document.getElementById('resultado');
    if (num1 !== '' && num2 !== '') {
        let a = Math.max(num1, num2);
        let b = Math.min(num1, num2);
        let resto = a % b;
    
        while (resto !== 0) {
            a = b;
            b = resto;
            resto = a % b;
        }
        resultado.textContent = `MDC(${num1}, ${num2} = ${b})`;
    } else {
        resultado.textContent = 'Preencha todos os campos!';
    }
    return false;
}
