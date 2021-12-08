function retornaHora(date) {
    if (date && !(date instanceof Date)) throw new TypeError('Esperando instância de Date.');

    if (!date) date = new Date();

    return date.toLocaleTimeString('pt-BR', {
    });
}

const timer = setInterval(() => {
  console.log(retornaHora());
}, 1000);

setTimeout(() => {
    clearInterval(timer);
}, 20000);