algoritmo "mediaabc"
var
  N1: real
  N2: real
  Nota: real
inicio
      Escreval("-------------------------")
      Escreval("ESCOLA")
      Escreval("-------------------------")
      Escreva("Primeira nota: ")
      Leia(N1)
      Escreva("Segunda nota: ")
      Leia(N2)
      Nota <- (N1 + N2) / 2
      Se (Nota >= 9) entao
         Escreval("A média do aluno é: ", Nota)
         Escreval("Aproveitamento: A")
      Senao
           Se (Nota >=8) e (Nota <8.9) entao
               Escreval("A média do aluno é: ", Nota)
               Escreval("Aproveitamento: B")
           Senao
              Se(Nota >=7) e (Nota <7.9) entao
              Escreval("A média do aluno é: ", Nota)
              Escreval("Aproveitamento: C")
           Senao
              Se (Nota >= 6) e (Nota <6.9) entao
                    Escreval("A média do aluno é: ", Nota)
                    Escreval("Aproveitamento: D")
                 Senao
                 Se (Nota >=5 ) e (Nota < 5.9) entao
                       Escreval("A média do aluno é: ", Nota)
                       Escreval("Aproveitamento: E")
                 Senao
                          Escreval("A média do aluno é: ", Nota)
                          Escreval("Aproveitamento: F")
                       FimSe
                 FimSe
           FimSe
      FimSe
      FimSe

fimalgoritmo
