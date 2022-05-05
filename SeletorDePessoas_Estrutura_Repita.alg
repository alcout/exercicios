algoritmo "SeletorDePessoas"
var
   S: Caractere
   I: Inteiro
   C: caractere
   Continuar: Caractere
   ContCMC:inteiro
   ContCFL:inteiro

inicio
      ContCMC <- 0
      ContCFL <- 0
      Repita
            Escreval("=======================")
            Escreval("  SELETORDE PESSOAS    ")
            Escreval("=======================")
            Escreva("Qual o sexo? [M/F]: ")
            Leia(S)
            Escreva("Qual a idade? : ")
            Leia(I)
            Escreval("Qual a cor do cabelo?: ")
            Escreval("----------------------")
            Escreval(" [1] Preto ")
            Escreval(" [2] Castanho ")
            Escreval(" [3] Loiro ")
            Escreval(" [4] Ruivo")
            Leia(C)
            Se (S = "M") e (I >=18) e (C = "2") entao
               ContCMC <- ContCMC + 1
            Fimse
            Se (S = "F") e (I >= 25) e (I <= 30) e (C = "3") entao
               ContCFL <- ContCFL + 1
            Fimse
            Escreval("Quer continuar? [S/N]")
            Leia(Continuar)
      Ate(Continuar = "N")
      Escreval("A quantidade de homens maiores de 18 anos e com cabelo castanho é: ", ContCMC)
      Escreval("A quantidade de mulheres entre 25 e 30 anos loiras é: ", ContCFL)
fimalgoritmo
