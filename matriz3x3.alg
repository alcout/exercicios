algoritmo "Matriz3x3"

var
    valores: vetor [1..3, 1..3] de inteiro
    l, c: inteiro

inicio
      Para l <- 1 ate 3 faca
           Para c <- 1 ate 3 faca
                Escreva("Digite o vetor da posição [", l, ",", c, "] :")
                Leia(valores[l,c])
           FimPara
      FimPara
      
      Para l <- 1 ate 3 faca
           Para c <- 1 ate 3 faca
                Se (valores[l,c] % 2 = 0) entao
                   Escreva("{", valores[l,c]:2, "}")
                senao
                   Escreva(valores[l,c]:4)
                Fimse
           FimPara
           Escreval()
      FimPara
fimalgoritmo
