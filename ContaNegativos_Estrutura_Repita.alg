algoritmo "ContaNegativos"
var
   N: Inteiro
   C: Inteiro
   TotalN:Inteiro

inicio

      C <-1
      TotalN <- 0
      Repita
         Escreva("Digite um numero: ")
         Leia (N)
         Se ( N < 0) entao
            TotalN <- TotalN + 1
         FimSE
         C <- C + 1
      Ate(C > 5)
      Escreval ("Foram digitados" , TotalN, " valores negativos.")
fimalgoritmo
