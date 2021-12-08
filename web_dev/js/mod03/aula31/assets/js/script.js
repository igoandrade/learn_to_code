const timerDisplay = document.querySelector('.timer');
const btnIniciar = document.querySelector('.btn-iniciar');
const btnPausar = document.querySelector('.btn-pausar');
const btnContinuar = document.querySelector('.btn-continuar');
const btnZerar = document.querySelector('.btn-zerar');
const btnVolta = document.querySelector('.btn-volta');
const tblVolta = document.querySelector('.tbl-volta');
const tbodyVolta = document.querySelector('.tbody-volta');

let milliseconds = 0;
let timer;
let timerData = {
    volta: [],
    tempoGeral: []
};

const formatTime = (milliseconds) => {
    const date = new Date(milliseconds);
    const centiseconds = Math.floor(date.getMilliseconds() / 10);
    return date.toLocaleTimeString('pt-BR', {
        hour12: false,
        minute:'2-digit',
        second:'2-digit',
        timeZone: 'GMT'
    }) + `.${centiseconds.toString().padStart(2, '0')}`;
};

const startTimer = (dt = 50) => {
    timer = setInterval(() => {
        milliseconds += dt;
        timerDisplay.innerHTML = formatTime(milliseconds);
    }, dt);
};

const initTimer = () => {
    btnIniciar.style.display = 'none';
    btnZerar.style.display = 'none';
    btnPausar.style.display = 'inline';
    btnVolta.style.display = 'inline';
    clearInterval(timer);
    startTimer();
};

const pauseTimer = () => {
    btnContinuar.style.display = 'inline';
    btnZerar.style.display = 'inline';
    btnPausar.style.display = 'none';
    btnVolta.style.display = 'none';
    timerDisplay.style.color = 'brown';
    clearInterval(timer);
};

const continueTimer = () => {
    btnContinuar.style.display = 'none';
    btnZerar.style.display = 'none';
    btnPausar.style.display = 'inline';
    btnVolta.style.display = 'inline';
    timerDisplay.style.color = 'white';
    startTimer();
};

const zeroTimer = () => {
    timerDisplay.innerHTML = '00:00.00';
    btnIniciar.style.display = 'inline';
    btnPausar.style.display = 'none';
    btnContinuar.style.display = 'none';
    timerDisplay.style.color = 'white';
    tblVolta.style.display = 'none';

    milliseconds = 0;
    tbodyVolta.innerHTML = '';
    timerData = {
        volta: [],
        tempoGeral: []
    };
};

const partialTimer = () => {
    tblVolta.style.display = 'inline';
    timerData['tempoGeral'].push(milliseconds);
    if (timerData['volta'].length === 0) {
        timerData['volta'].push(milliseconds);
    } else {
        timerData['volta'].push(milliseconds - timerData['volta'][timerData['volta'].length - 1]);
    }
    let i = timerData['volta'].length - 1;
    let volta = timerData['volta'][i];
    let geral = timerData['tempoGeral'][i];
    tbodyVolta.innerHTML = `<tr>
        <td>${(i+1).toString().padStart(2, ' ')}</td>
        <td>${formatTime(volta)}</td>
        <td>${formatTime(geral)}</td>
    </tr>` + tbodyVolta.innerHTML;
};
