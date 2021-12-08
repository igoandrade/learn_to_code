function retornaHora(date) {
    if (date && !(date instanceof Date)) throw new TypeError('Esperando instância de Date.');

    if (!date) date = new Date();

    return date.toLocaleTimeString('pt-BR', {
    });
}


try {
    const data = new Date('08-27-1985 06:01:32');
    const hora = retornaHora(data);
    console.log(hora);
} catch (e) {
    console.log(e);
} finally {
    console.log('Finalizando programa.')
}
