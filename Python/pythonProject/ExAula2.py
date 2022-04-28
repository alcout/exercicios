class ExAula2:
     def ValorKM():
        km = float(input('Quantos km você percorreu em sua viagem?:'))
        dias = float(input('Quantos dias você ficou com o carro de aluguel?:'))
        carro = 60
        kmR = 0.15
        totalDia = (km * 0.15) + (dias * 60)
        print('O total a ser pago por {} dias e por {} km rodados será no valor de R${}'. format(dias, km, totalDia))











