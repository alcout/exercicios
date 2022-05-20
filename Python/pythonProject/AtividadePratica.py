class Ex1AP:
    def LojaVirtual():
        print('Bem vindo a loja da Ana Lucia da Costa Coutinho RU:3932630')#Menu de entrada
        ValorProduto = float(input('Entre com o valor do produto:'))#console lerá o valor do produto
        QuantidadeProduto = int(input('Entre com a quantidade de produto:'))#console lerá quantidade do produto
        ValorSubtotal = ValorProduto * QuantidadeProduto

        if QuantidadeProduto <= 9:
            ValorTotal = ValorSubtotal
        elif QuantidadeProduto >= 10 and QuantidadeProduto <= 99:
            ValorTotal = ValorSubtotal - ValorSubtotal * 0.05
        elif QuantidadeProduto >= 100 and QuantidadeProduto <=999:
            ValorTotal = ValorSubtotal - ValorSubtotal * 0.10
        else:
            ValorTotal = ValorSubtotal - ValorSubtotal * 0.15
        print('O valor sem desconto foi de R${:.2f}'.format(ValorSubtotal))
        print('O valor com desconto foi de R${:.2f}'.format(ValorTotal))
        #utilizado ':.2f' para os números decimais ficarem com somente duas casas depois da vírgula

    def Lanchonete():
        #Menu de entrada
        print('----------------------------------------------------------------')
        print('BEM VINDO A LANCHONETE DA ANA LUCIA DA COSTA COUTINHO RU:3932630')
        print('----------------------------------------------------------------')
        print('                    CARDÁPIO                            ')
        print('----------------------------------------------------------------')
        print('|  Código  |        Descrição           |   Valor  |')
        print('|    100   |     Cachorro-Quente        |   R$9,00 |')
        print('|    101   |     Cachorro-Quente Duplo  |  R$11,00 |')
        print('|    102   |     X-Egg                  |  R$12,00 |')
        print('|    103   |     X-Salada               |  R$13,00 |')
        print('|    104   |     X-Bacon                |  R$14,00 |')
        print('|    105   |     X-Tudo                 |  R$17,00 |')
        print('|    200   |     Refrigerante Lata      |   R$5,00 |')
        print('|    201   |     Chá Gelado             |   R$4,00 |')

        total = 0 #esse valor precisa iniciar em 0, pois é o valor inicial de quando ainda não foi pedido nada.

        while True:
            pedido = int(input('Entre com o código desejado:'))
            if pedido == 100:
                total += 9.00 #total vai ir guardando o valor da compra
                print('Você pediu um Cachorro-Quente de R$9,00')
            elif pedido == 101:
                total += 11.00
                print('Você pediu um Cachorro-Quente Duplo de R$11,00')
            elif pedido == 102:
                total += 12.00
                print('Você pediu um X-Egg de R$12,00')
            elif pedido == 103:
                total += 13.00
                print('Você pediu um X-Salada de R$13,00')
            elif pedido == 104:
                total += 14.00
                print('Você pediu um X-Bacon de R$14,00')
            elif pedido == 105:
                total += 17.00
                print('Você pediu um X-Tudo de R$17,00')
            elif pedido == 200:
                total += 5.00
                print('Você pediu um Refrigerante de R$5,00')
            elif pedido == 201:
                total += 4.00
                print('Você pediu um Chá Gelado de R$4,00')
            else:
                print('Opção Inválida')
                continue
            print('Deseja pedir mais alguma coisa?')
            print('1 - Sim')
            print('0 - Não')
            continuarpedidos = input('>>')

            if continuarpedidos == '1':#o valor está dentro de aspas pois foi tratado como string.
                continue #o continue vai voltar no inicio do código
            elif continuarpedidos == '0':
                print('O valor total a ser pago é R$ {:.2f}'.format(total))
                break #vai finalizar o looping saindo do while true


    #exercício 3 atividade prática
    #início da função DimensõesObjeto
    def DimensoesObjeto(self):
        while True:
            try:
                ValorObjeto = 0
                AlturaObjeto = int(input('Qual a altura do objeto (em cm):'))
                LarguraObjeto = int(input('Qual a largura do objeto (em cm):'))
                ComprimentoObjeto = int(input('Qual o comprimento do objeto (em cm):'))
                VolumeObjeto = AlturaObjeto * LarguraObjeto * ComprimentoObjeto
                print('O volume do objeto é (em cm³):{}'.format(VolumeObjeto))

                if (VolumeObjeto <= 1000):
                    ValorObjeto = 10
                elif (VolumeObjeto >= 1001) and (VolumeObjeto <= 10000):
                    ValorObjeto = 20
                elif (VolumeObjeto >= 10001) and (VolumeObjeto <= 30000):
                    ValorObjeto = 30
                elif (VolumeObjeto >= 30001) and (VolumeObjeto <= 100000):
                    ValorObjeto = 50
                else:
                    print('Não aceitamos objeto com dimensões tão grande.')
                    continue
            except:
                print('Você digitou alguma dimensão do objeto com valor não numérico.')
                print('Por favor, entre com as dimensões desejadas novamente.')
                continue
            else:
                return VolumeObjeto
    #Fim da função DimensõesObjeto

    #início da função PesoObjeto
    def PesoObjeto(self):
        while True:
            try:
                multiplicadorObjeto = 0
                PesoObjeto = float(input('Digite o peso do objeto (em kg):'))
                if (PesoObjeto <= 0.10):
                    multiplicadorObjeto = 1
                elif (PesoObjeto >= 0.11) and (PesoObjeto <= 1):
                    multiplicadorObjeto = 1.5
                elif (PesoObjeto >= 1.10) and (PesoObjeto <= 10):
                    multiplicadorObjeto = 2
                elif (PesoObjeto >= 10.1) and (PesoObjeto <= 30):
                    multiplicadorObjeto = 3
                else:
                    print('Não aceitamos objetos tão pesados')
                    continue
            except:
                print('Você digitou peso do objeto com valor não numérico.')
                print('Por favor, entre com o peso desejado novamente.')
                continue
            else:
                return multiplicadorObjeto
    #Fim da função PesoObjeto

    #início da função RotaObjeto
    def RotaObjeto(self):
        while True:
            try:
                multiplicadorRota = 0
                print('Selecione a rota:')
                print('RS - De Rio de Janeiro até São Paulo')
                print('SR - De São Paulo até Rio de Janeiro')
                print('BS - De Brasília até São Paulo')
                print('SB - De São Paulo até Brasília')
                print('BR - De Brasília até Rio de Janeiro')
                print('RB - Rio de Janeiro até Brasília')
                rota = input()
                if (rota == 'RS'):
                    multiplicadorRota = 1
                elif (rota == 'SR'):
                    multiplicadorRota = 1
                elif (rota == 'BS'):
                    multiplicadorRota = 1.2
                elif (rota == 'SB'):
                    multiplicadorRota = 1.2
                elif (rota == 'BR'):
                    multiplicadorRota = 1.5
                elif (rota == 'RB'):
                    multiplicadorRota = 1.5
                else:
                    print('Você digitou uma rota inexistente.')
                    print('Por favor, entre com a rota desejada novamente.')
                    continue
            except:
                print('Você digitou uma rota inexistente.')
                print('Por favor, entre com a rota desejada novamente.')
                continue
            return multiplicadorRota
    #Fim da função RotaObjeto

    #início da função EmpresaEntrega
    def EmpresaEntrega(self):
        print('Bem Vindo a Companhia de Logística Ana Lúcia da Costa Coutinho RU:3932630 ')
        VolumeObjeto = self.DimensoesObjeto()
        multiplicadorObjeto = self.PesoObjeto()
        multiplicadorRota = self.RotaObjeto()
        ValorFinal = (VolumeObjeto) * (multiplicadorObjeto) * (multiplicadorRota)
        print('O total a ser pago é:R$ {:.2f} (dimensões:{:.2f} * peso: {:.2f} * rota: {:.2f})'.format(ValorFinal,VolumeObjeto, multiplicadorObjeto,multiplicadorRota))
    #fim da função EmpresaEntrega
    #fim exercício 3
















