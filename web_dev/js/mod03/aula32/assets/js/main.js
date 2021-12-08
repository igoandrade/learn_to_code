const timerDisplay = document.querySelector('.timer');
const btnIniciar = document.querySelector('.btn-iniciar');
const btnPausar = document.querySelector('.btn-pausar');
const btnContinuar = document.querySelector('.btn-continuar');
const btnZerar = document.querySelector('.btn-zerar');
const btnVolta = document.querySelector('.btn-volta');
const tblVolta = document.querySelector('.tbl-volta');
const tbodyVolta = document.querySelector('.tbody-volta');

let startTime;
let baseTime = 0;
let miliseconds = 0;
let timeText;
let timer;

let timerData = {
    volta: [],
    tempoGeral: []
};

const getDiffTime = (startTime, endTime=Date.now()) => {
    return endTime - startTime;
};

const formatTime = (miliseconds) => {
    let centiseconds = Math.floor(miliseconds / 10);
    let minutes = Math.floor(centiseconds / 6000);
    let seconds = Math.floor((centiseconds % 6000) / 100);
    centiseconds -= 6000 * minutes + 100 * seconds;
    return `${minutes.toString().padStart(2,'0')}:${seconds.toString().padStart(2,'0')}:${centiseconds.toString().padStart(2,'0')}`;
};

const initTimer = () => {
    startTime = new Date().getTime();
    btnIniciar.style.display = 'none';
    btnZerar.style.display = 'none';
    btnPausar.style.display = 'inline';
    btnVolta.style.display = 'inline';
    timer = setInterval(() => {
        miliseconds = getDiffTime(startTime);
        timeText = formatTime(miliseconds);
        timerDisplay.innerHTML = timeText;
    }, 50);
    
};

const pauseTimer = () => {
    clearInterval(timer);
    baseTime = miliseconds;
    btnContinuar.style.display = 'inline';
    btnZerar.style.display = 'inline';
    btnPausar.style.display = 'none';
    btnVolta.style.display = 'none';
    timerDisplay.style.color = 'brown';
}


const continueTimer = () => {
    startTime = new Date().getTime();
    timer = setInterval(() => {
        miliseconds = baseTime + getDiffTime(startTime);
        timeText = formatTime(miliseconds);
        timerDisplay.innerHTML = timeText;
    }, 50);
    
    btnContinuar.style.display = 'none';
    btnZerar.style.display = 'none';
    btnPausar.style.display = 'inline';
    btnVolta.style.display = 'inline';
    timerDisplay.style.color = 'dimgray';
    
}

const zeroTimer = () => {
    clearInterval(timer);
    timerDisplay.innerHTML = '00:00.00';
    btnIniciar.style.display = 'inline';
    btnPausar.style.display = 'none';
    btnContinuar.style.display = 'none';
    timerDisplay.style.color = 'dimgray';
    tblVolta.style.display = 'none';
    tbodyVolta.innerHTML = '';
    timerData = {
        volta: [],
        tempoGeral: []
    };
};

const voltaTimer = () => {
    tblVolta.style.display = 'inline';
    timerData['tempoGeral'].push(miliseconds);
    if (timerData['volta'].length === 0) {
        timerData['volta'].push(miliseconds);
    } else {
        timerData['volta'].push(miliseconds - timerData['volta'][timerData['volta'].length - 1]);
    }
    let i = timerData['volta'].length - 1;
    let volta = timerData['volta'][i];
    let geral = timerData['tempoGeral'][i];
    tbodyVolta.innerHTML = `<tr>
        <td>${(i+1).toString().padStart(2, ' ')}</td>
        <td>${formatTime(volta)}</td>
        <td>${formatTime(geral)}</td>
    </tr>` + tbodyVolta.innerHTML;

    //timerData['tempoGeral'].push(miliseconds);
};
