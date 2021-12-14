function Calculadora() {
    this.display = document.querySelector('.display');
    this.ans = '';

    this.inicia = () => {
        this.capturaCliques();
        this.capturaEnter();
    }

    this.addNumDisplay = element => {
        if (!this.display.value.includes('(') && element.innerText===')') return;

        if (!this.display.value && element.classList.contains('btn-symbol')) return;

        if (this.ans && element.classList.contains('btn-num')) {
            this.display.value = element.innerText;
            this.display.focus();
            return;
        }

        if (this.display.value && element.innerText==='(') {
            this.display.value += '*(';
            this.ans = '';
            this.display.focus();
            return;
        }
        this.display.value += element.innerText;
        this.display.focus();
        this.ans = '';
        
    }

    this.clear = () => this.display.value = '';

    this.del = () => this.display.value = this.display.value.slice(0, -1);

    this.realizaConta = () => {
        try {
            let operacao = this.display.value;
            const regExp = /[a-zA-Z]/g;
            if (regExp.test(operacao)) {
                alert('Operação inválida!!!');
                this.display.value = '';
                this.ans = '';
                return;
            } else {
                operacao = eval(operacao);
                if (!operacao) {
                    alert('Operação inválida!!');
                    this.display.value = '';
                    this.ans = '';
                    return;
                }
            }
            this.display.value = operacao;
            this.ans = operacao;
        } catch (err) {
            alert('Operação inválida!');
            this.display.value = '';
            this.ans = '';
            return;
        }
    }

    this.capturaCliques = () => {
        document.addEventListener('click', event => {
            const element = event.target;

            if (element.classList.contains('btn-num')) this.addNumDisplay(element);
            if (element.classList.contains('btn-symbol')) this.addNumDisplay(element);
            if (element.classList.contains('btn-dot')) this.addNumDisplay(element);
            if (element.classList.contains('btn-clear')) this.clear();
            if (element.classList.contains('btn-del')) this.del();
            if (element.classList.contains('btn-equal')) this.realizaConta();
        });
    }    

    this.capturaEnter = () => {
        document.addEventListener('keypress', e => {
            if (e.code !== "Enter" && e.code !== "NumpadEnter") return;
            this.realizaConta();
            this.display.focus();
        })
    }
}

const calculadora = new Calculadora();
calculadora.inicia();
//Fim