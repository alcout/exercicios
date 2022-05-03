class ExAula4:
    def SequenciaNumerosW():
        I3a12 = 3
        while (I3a12 <= 12):
            print(I3a12)
            I3a12 += 1

    def SequenciaNumerosF():
        I0a9 = 0
        for I0a9 in range(0,9,2):
                print(I0a9)

    def CalculadoraAprimorada():
        Valor1 = int(input('Digite o primeiro número:'))
        Valor2 = int(input('Digite o segundo número: '))
        print('OPERAÇÕES:')
        print('Adição +')
        print('Subtração -')
        print('Divisão /')
        print('Multiplicação *')
        Operacao = input('Qual a operação você deseja fazer?')
        while(Operacao != 's'):
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
            Valor1 = int(input('Digite o primeiro número:'))
            Valor2 = int(input('Digite o segundo número: '))
            print('OPERAÇÕES:')
            print('Adição +')
            print('Subtração -')
            print('Divisão /')
            print('Multiplicação *')
            Operacao = input('Qual a operação você deseja fazer?')

        print('Encerrando o programa...')

    def CaixaEletronico():
        valor = int(input('Digite o valor que você deseja sacar:R$'))
        while True:
            if valor >= 100 :
                cedulas100 = valor // 100
                valor -= cedulas100 * 100
                print('Cédulas de R$100: {}'.format(cedulas100))
                if not valor:
                    break
            if valor >= 50 :
                cedulas50 = valor // 50
                valor -= cedulas50 * 50
                print('Cédulas de R$50: {}'.format(cedulas50))
                if not valor:
                    break
            if valor >= 20 :
                cedulas20 = valor // 20
                valor -= cedulas20 * 20
                print('Cédulas de R$20: {}'.format(cedulas20))
                if not valor:
                    break
            if valor >= 10 :
                cedulas10 = valor // 10
                valor -= cedulas10 * 10
                print('Cédulas de R$10: {}'.format(cedulas10))
                if not valor:
                    break
            if valor >= 5 :
                cedulas5 = valor // 5
                valor -= cedulas5 * 5
                print('Cédulas de R$5: {}'.format(cedulas5))
                if not valor:
                    break
            if valor:
                cedulas1 = valor
                print('Cédulas de R$1: {}'.format(cedulas1))
                break

    def BilheteriaCinema():
        print('-------BILHETERIA-------')
        print('Valores:')
        print('-> Menores de 3 anos não pagam')
        print('-> Entre 3 e 12 anos: R$15')
        print('-> Acima de 12 anos: R$30')
        total = 0
        dinheiro = 0
        while True:
            idade = (input('Qual a sua idade?:'))
            if idade == 'sair':
                break
            idade = int(idade)
            total += 1
            if idade < 3:
                ingresso = 0
                print('O valor de seu ingresso será de R$0')

            if idade >= 3 and idade <=12 :
                ingresso = 15
                print('O valor de seu ingresso será de R$ 15')

            if idade >12 :
                ingresso = 30
                print('O valor de seu ingresso será de R$30')
            dinheiro += ingresso
        media = dinheiro /total
        print('O total de pessoas é : {}'.format(total))
        print('O total arrecadado é : {}'.format(dinheiro))
        print('A média arrecadada é : {}'.format(media))









