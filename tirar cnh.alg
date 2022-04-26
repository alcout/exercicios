algoritmo "Tirar cnh"
var
  Ano: inteiro
  Nascimento: inteiro
  Idade: inteiro
inicio
      Escreval("-------------------------")
      Escreval("DEPARTAMENTO DE TRÂNSITO")
      Escreval("-------------------------")
      Escreva("Ano atual(yyyy): ")
      Leia(Ano)
      Escreva("Ano de nascimento(yyyy): ")
      Leia(Nascimento)
      Idade <- Ano - Nascimento
      Se (Idade >= 18) entao
         Escreval("---------STATUS---------")
         Escreval("Idade: ", Idade, " anos")
         Escreval("APTO A TIRAR A CARTEIRA")
         Escreval("-------------------------")
      Senao
           Escreval("---------STATUS---------")
         Escreval("Idade: ", Idade, " anos")
         Escreval("INAPTO A TIRAR A CARTEIRA")
         Escreval("-------------------------")
      FimSe

fimalgoritmo
