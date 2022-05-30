algoritmo "Analisador de Valores"

var
        Cont:inteiro
        N: inteiro
        S:inteiro
        M:Real
        D5:inteiro
        Nulos : inteiro
        SomaP:inteiro
inicio
      Cont <- 1
      S <- 0
      D5 <-0
      Para Cont <- 1 ate 5 faca
           escreval("Digite o", Cont , "° valor:" )
           leia (N)
           S <- S + N
           Se (N%5=0)   entao
              D5 <- D5 + 1
           FimSe
           Se (N = 0) entao
              Nulos <- Nulos + 1
           FimSe
           Se (N%2=0) entao
              SomaP <- SomaP + N
           FimSe
           
      FimPara
      M <- S / 5
      Escreval("A soma dos valores é:", S)
      Escreval("A média dos valores é:" , M)
      Escreval(D5, " são divisíveis por 5")
      Escreval(Nulos, " números são nulos")
      Escreval("A soma dos pares é: ", SomaP)
      
      


fimalgoritmo
