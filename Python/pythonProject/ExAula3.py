class ExAula3:
    def CalculeIdade():
         AnoAtual = int(input('Qual o ano atual?:'))
         AnoNascimento = int(input('Qual o ano em que você nasceu?:'))

         Idade = AnoAtual - AnoNascimento

         if (Idade >= 18):
            print('Parabéns! Você já pode tirar a sua habilitação de motorista!!!')

    def BonusSalario():
        SalarioAtual = float(input("Qual o seu salário atual?"))
        TempoDeEmpresa = float(input('Quantos anos você está na empresa?'))

        if (TempoDeEmpresa > 5):
            Bonus = (SalarioAtual * 20) /100
            SalarioBonificacao = SalarioAtual + Bonus

        else:
            Bonus = (SalarioAtual * 10) /100
            SalarioBonificacao = SalarioAtual + Bonus

        print('O seu Salário com bonificação será de {}'.format(SalarioBonificacao))

    def Calculadora():
        Valor1 = int(input('Digite um número:'))
        Valor2 = int(input('Digite outro número:'))

        Operacao = input('Qual a operação você deseja realizar? [+] [-] [*] [/]:')

        if (Operacao == '+'):
            Soma = Valor1 + Valor2
            print('A soma de {} com {} é {}'.format(Valor1,Valor2,Soma))
        elif(Operacao == '-'):
            Subtracao = Valor1 - Valor2
            print('A subtração de {} com {} é {}'.format(Valor1, Valor2, Subtracao))
        elif(Operacao == '*'):
            Multiplicacao = Valor1 * Valor2
            print('A multiplicação de {} com {} é {}'.format(Valor1, Valor2, Multiplicacao))
        elif(Operacao == '/'):
            Divisao = Valor1 / Valor2
            print('A divisão de {} com {} é {}'.format(Valor1, Valor2, Divisao))
















