algoritmo "Tabuada"
var
    Cont: inteiro
    N: inteiro
    R: inteiro
inicio
      Cont <- 1
      Escreva ("Quer ver a tabuada de qual numero? [1 a 10] ")
      Leia(N)
      Repita
          R <- N * Cont
          Escreval(N, " X " , Cont, " = ", R)
          Cont <- Cont + 1
      Ate (Cont > 10)
fimalgoritmo
