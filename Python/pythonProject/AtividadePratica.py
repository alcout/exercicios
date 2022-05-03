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
















