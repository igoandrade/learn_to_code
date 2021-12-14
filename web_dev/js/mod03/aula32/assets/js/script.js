const formTarefas = document.querySelector('.form-tarefas');
const inputTarefa = document.querySelector('#input-tarefa');
const tblTarefas = document.querySelector('.tbl-tarefas');
const tbodyTarefas = document.querySelector('.tbody-tarefas');

formTarefas.addEventListener('submit', (e) => {
    e.preventDefault();
});

const saveTasks = () => {
    const tdTasks = tbodyTarefas.querySelectorAll('.descricao-tarefa');
    let listaDeTarefas = [];
    for (let task of tdTasks) {
        let descricaoTarefa = task.innerText;
        listaDeTarefas.push(descricaoTarefa.trim());
    }
    const tarefasJSON = JSON.stringify(listaDeTarefas);
    localStorage.setItem('tarefas', tarefasJSON);

};

const addTarefa = () => {
    if (!inputTarefa.value) return;
    let tarefa = inputTarefa.value;
    printTarefa(tarefa);
    inputTarefa.value = '';
    saveTasks();
};

document.addEventListener('click', (e) => {
    const element = e.target;
    if (element.classList.contains('btn-remove')) {
        element.parentElement.parentElement.remove();
        saveTasks();
    }
});


const printTarefa = (tarefa) => {
    tbodyTarefas.innerHTML += `<tr>
        <td class="descricao-tarefa">${tarefa}</td>
        <td>
            <button class="btn-remove">X</button>
        </td>
    </tr>`;
};


const getTasksFromLocalStorage = () => {
    const tasks = localStorage.getItem('tarefas');
    console.log(tasks);
    const listOfTasks = JSON.parse(tasks);
    
    for (let tarefa of listOfTasks) {
        printTarefa(tarefa);
    }
};

getTasksFromLocalStorage();


