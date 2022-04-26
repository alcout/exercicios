algoritmo "Fatorial"
var
        N: inteiro
        Cont: inteiro
        F: Inteiro
inicio

      Escreva("Digite um numero para saber o seu fatorial: ")
      Leia(N)
      Cont <- N
      F <- 1
      
      Repita
            F <- F * Cont
            Cont <- Cont - 1
      Ate(Cont < 1)
      Escreval(" O valor do fatorial de" , N, " é ", F)
fimalgoritmo
