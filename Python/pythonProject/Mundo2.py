from time import sleep
from random import randint
class Mundo2:
    def ex36():
        print('Bem vindo ao Banco')
        print('----------------------------------')
        print('Solicitação de Empréstimo Bancário')
        print('----------------------------------')
        casa = float(input('Qual o valor da casa?'))
        salario = float(input('Qual o seu salário?'))
        anos = float(input('Em quantos anos você deseja pagar?'))
        prestacao = casa / (anos * 12)
        print('Para pagar uma casa de R${:.2f}'.format(casa), end='')
        print(' em {} anos, a prestação será {:.2f}'.format(anos,prestacao))

        if (prestacao) > (salario * 0.3):
            print('O Empréstimo foi negado pois a prestação será {:.2f}'.format(prestacao))
        else:
            print('O empréstimo foi concedido e a prestação será de {:.2f}'.format(prestacao))

    def ex37():
        num = int(input('Digite um número inteiro:'))
        print('''Escolha uma das bases para conversão:
        [1]converter para BINÁRIO
        [2]converter para OCTAL
        [3] converter para HEXADECIMAL''')
        opção = int(input('Sua opção: '))

        if opção == 1:
            print('{} convertido para BINÁRIO é {}'.format(num, bin(num)))
        elif opção == 2:
            print('{} convertido para OCTAL é {}'.format(num, oct(num)))
        elif opção == 3:
            print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)))
        else:
            print('Opção inválida')

    def ex38():
        num1 = int(input('Digite o primeiro número inteiro: '))
        num2 = int(input('Digite o segundo número inteiro: '))

        if num1 > num2:
            print('O primeiro número é maior do que o segundo.')
        elif num2 > num1:
            print('O segundo número é maior do que o primeiro')
        else:
            print('Os dois valores são iguais.')

    def ex46():
        print('{:=^40}'.format(' CONTAGEM REGRESSIVA '))
        for c in range(10, -1, -1):
            print(c)
            sleep(0.5)
        print('*****BUMMMMM!*****')

    def ex47():
        for c in range(1,51):
            if c % 2 == 0:
                print(c, end=' ')

    def ex48():
        soma = 0
        for n in range (1,501):
            if (n % 2 != 0) and (n % 3 == 0):
                soma = soma + n
        print(f'A soma de todos os números divisíveis por 3 e ímpares é {soma}')

    def ex66():
        soma = 0
        cont = 0
        while True:
            n = int(input('Digite um número inteiro(999 encerra):'))
            if n != 999:
                soma += n
                cont += 1
            else:
                break
        print(f'Foram digitados {cont} números e a soma deles é {soma}')

    def ex68():
        while True:
            totalJogadas = 0
            somaJ = 0
            jogador = int(input('Digite um valor inteiro:'))
            jogada = str(input('Par [P] ou Ímpar [I]?:')).upper()
            computador = randint(0, 10)
            total = jogador + computador
            print(f'Você jogou {jogador} e o computador jogou {computador} e o total foi {total}.')
            if total % 2 == 0 and jogada == 'P':
               somaJ += 1
               totalJogadas += 1

            elif total % 2 != 0 and jogada == 'I':
               somaJ += 1
               totalJogadas += 1

            else:
                print(f'O total de vitórias consecutivas foram {totalJogadas}.')
                break





















