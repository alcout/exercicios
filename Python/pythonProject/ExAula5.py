class ExAula5:
    def Borda(s1):
        tam = len(s1)
        if tam:
            print('+','-' * tam, '+')
            print('|', s1, '|')
            print('+', '-' * tam, '+')

    def Contagem(fim, inicio = 0, passo = 1):
        for resp in range (inicio,fim,passo):
            print('{} '.format(resp), end='')
        print('\n')

    def ValoresOrdenados():
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
        valor3 = int(input('Digite o terceiro valor: '))

        if valor1 < valor2 and valor2 < valor3 :
            print('{} , {} , {} ,'.format(valor1,valor2,valor3), end='')
        elif valor2 < valor1 and valor1 < valor3 :
            print('{} , {} , {} ,'.format(valor2, valor1, valor3), end='')
        elif valor3 < valor1 and valor1 < valor2:
            print('{} , {} , {} ,'.format(valor3, valor1, valor2), end='')
        elif valor1 < valor3 and valor3 < valor2:
            print('{} , {} , {} ,'.format(valor1, valor3, valor2), end='')
        elif valor2 < valor3 and valor3 < valor1:
            print('{} , {} , {} ,'.format(valor2, valor3, valor1), end='')
        else:
            print('{} , {} , {} ,'.format(valor3, valor2, valor1), end='')

    def valida_int(self, pergunta, min, max):
        x = int(input(pergunta))
        while ((x < min) or (x > max)):
            x = int(input(pergunta))
        return x

    def fatorial(self):
        num = self.valida_int('Digite um valor para calcularo seu fatorial:', 0, 9999)
        fat = 1
        if num == 0:
            return fat
        for i in range(1, num+1, 1):
            fat = fat * i
        print('{}! = {}'.format(num, fat))



























