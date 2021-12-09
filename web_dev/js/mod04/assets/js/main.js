function criaCalculadora() {
    return {
        display: document.querySelector('.display'),
        btnClear: document.querySelector('.btn-clear'),
        operacaoRealizada: false,

        inicia() {
            this.cliqueBotoes();
            this.pressionaEnter();
        },

        clearDisplay() {
            this.display.value = '';
        },

        apagaUm() {
            this.display.value = this.display.value.slice(0, -1);
        },

        realizaOperacao() {
            let operacao = this.display.value;

            try {
                operacao = eval(operacao);

                this.display.value = String(operacao);
                this.operacaoRealizada = true;
            } catch (err) {
                this.display.value = '';
                this.operacaoRealizada = true;
                alert('Operação inválida.');
            }
        },

        cliqueBotoes() {
            document.addEventListener('click', (event) => {
                const element = event.target;

                if(element.classList.contains('btn-math')) {
                    this.btnParaDisplay(element.innerText);
                }

                if (element.classList.contains('btn-clear')) {
                    this.clearDisplay();
                }

                if (element.classList.contains('btn-del')) {
                    this.apagaUm();
                }

                if (element.classList.contains('btn-equal')) {
                    this.realizaOperacao();
                }
            });
        },

        pressionaEnter() {
            this.display.addEventListener('keyup', (event) => {
                if (event.keyCode === 13) this.realizaOperacao();
            })
        },

        btnParaDisplay(valor) {
            if (this.operacaoRealizada) {
                this.display.value = '';  
                this.operacaoRealizada = false;
            } 
            this.display.value += valor;
            
        },
    };
}

const calculadora = criaCalculadora();
calculadora.inicia();