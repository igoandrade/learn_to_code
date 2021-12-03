function setFullDate() {
    let date = new Date();
    let dataCompleta = document.querySelector('#data-completa');
    let horaCompleta = document.querySelector('#hora-completa');
    let weekDayText = getWeekDay(date);
    let day = date.getDate().toString().padStart(2, '0');
    let monthText = getMonthText(date);
    let year = date.getFullYear();
    let hours = date.getHours().toString().padStart(2, '0');
    let minutes = date.getMinutes().toString().padStart(2, '0');
    let seconds = date.getSeconds().toString().padStart(2, '0');

    dataCompleta.innerHTML = `${weekDayText}, ${day} de ${monthText} de ${year}`;

    horaCompleta.innerHTML = `${hours}:${minutes}:${seconds}`;
}

function getWeekDay(date) {
    let weekDay = date.getDay();
    let weekDayText;
    switch (weekDay) {
        case 0: 
            weekDayText = 'Domingo';
            break;
        case 1: 
            weekDayText = 'Segunda-feira';
            break;
        case 2: 
            weekDayText = 'Terça-feira';
            break;
        case 3: 
            weekDayText = 'Quarta-feira';
            break;
        case 4: 
            weekDayText = 'Quinta-Feira';
            break;
        case 5: 
            weekDayText = 'Sexta-feira';
            break;
        case 6: 
            weekDayText = 'Sábado';
            break;
        default:
            weekDayText = '';
    }
    return weekDayText;
}

function getMonthText(date) {
    const months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
    return months[date.getMonth()];
}

setInterval(setFullDate, 0);