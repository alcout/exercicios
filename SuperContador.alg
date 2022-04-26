algoritmo "SuperContador"
var
      N:Inteiro
      Cont:Inteiro
inicio


      Repita
          Escreval("=================")
          Escreval("|   M E N U     |")
          Escreval("=================")
          Escreval("| [1] De 1 a 10 |")
          Escreval("| [2] De 10 a 1 |")
          Escreval("| [3] Sair      |")
          Escreval("=================")
          Leia(N)
                 Se (N = 1) entao
                    Cont <- 1
                    Repita
                          Escreva(Cont ,"..." )
                          Cont <- Cont + 1
                    Ate(Cont > 10)
                    Escreval(" ")
                 FimSe
                 
                 Se (N = 2)  entao
                    Cont <- 10
                    Repita
                          Escreva(Cont, "..." )
                          Cont <- Cont -1
                    Ate (Cont < 0)
                    Escreval(" ")
                 FimSe
               



      Ate(N = 3)

fimalgoritmo

