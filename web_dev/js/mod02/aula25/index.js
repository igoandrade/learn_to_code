// Objeto
const pessoa1 = {
    nome: "Igo",
    sobrenome: "Andrade",
    idade: "36"
};
document.getElementById("pessoa1").innerHTML += `<li>Nome: ${pessoa1.nome}</li>`;
document.getElementById("pessoa1").innerHTML += `<li>Sobrenome: ${pessoa1.sobrenome}</li>`;
document.getElementById("pessoa1").innerHTML += `<li>Idade: ${pessoa1.idade}</li>`;

function criaPessoa(nome, sobrenome, idade) {
    return {
        nome: nome,
        sobrenome: sobrenome,
        idade: idade
    };
}
const Pessoas = [];
Pessoas.push(criaPessoa('Igo', 'Andrade', 36));
Pessoas.push(criaPessoa('Lana', 'Lang', 25));
Pessoas.push(criaPessoa('Peter', 'Parker', 42));
Pessoas.push(criaPessoa('Fox', 'Mulder', 38));

for (pessoa of Pessoas) {
    document.getElementById("tbodyPesoas").innerHTML += `<tr><td>${pessoa.nome}</td><td>${pessoa.sobrenome}</td><td>${pessoa.idade}</td></tr>`;
}