algoritmo "CampeonatoFutebol"

var
   time: vetor[1..3] de Caractere
   p,i:inteiro
inicio
      Escreval("---------------------")
      Escreval("CAMPEONATO DE FUTEBOL")
      Escreval("---------------------")
      Para i <- 1 ate 3 faca
           Escreva("Digite o primeiro time:")
           Leia(time[i])
      FimPara
      LimpaTela
      Escreval("---------------------")
      Escreval("       PARTIDAS"      )
      Escreval("---------------------")
      Para p <- 1 ate 3 faca
           Para i <- 1 ate 3 faca
                Se (i <> p) entao
                Escreval(time[p], "X", time[i])
                FimSe
           FimPara
      FimPara

fimalgoritmo
