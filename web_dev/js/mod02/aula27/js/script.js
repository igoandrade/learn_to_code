function meuEscopo() {
    const form = document.querySelector('.form');
    const tabela = document.querySelector('.table');
    const tbody = document.querySelector('tbody');

    function criaPessoa(nome, sobrenome, peso, altura) {
        return {nome, sobrenome, peso, altura};
    }

   function recebeEventoForm (evento) {
        evento.preventDefault();
        const pessoas = [];
        const nome = form.querySelector('.nome');
        const sobrenome = form.querySelector('.sobrenome');
        const peso = form.querySelector('.peso');
        const altura = form.querySelector('.altura');
        pessoas.push(criaPessoa(nome.value, sobrenome.value, peso.value, altura.value));
        nome.value = '';
        sobrenome.value='';
        peso.value = '';
        altura.value = '';
        if (pessoas.length != 0) {
            for (pessoa of pessoas) {
                tbody.innerHTML += `<tr>
                    <td>${pessoa.nome} ${pessoa.sobrenome}</td>
                    <td>${pessoa.peso}</td>
                    <td>${pessoa.altura}</td>
                </tr>
                `;                
            };
        tabela.style.display = 'block';
        }


   };
   form.addEventListener('submit', recebeEventoForm);


}
meuEscopo();