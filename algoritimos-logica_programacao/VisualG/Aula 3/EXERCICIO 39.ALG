Algoritmo "Exercicio 39"

Var
   S,R,A:real


Inicio
      Escreva("Salário: ")
      Leia(S)
      se (S > 1000) entao
         A <- (S/100)*5
         R <- S+A
         Escreva("Novo Salário: R$",R)
      senao
           se (S>=500) e (S <= 1000) entao
           A <- (S/100)*10
           R <- S+A
           Escreva("Novo Salário: R$",R)
           senao
                se (S <= 499) entao
                 A <- (S/100)*15
                 R <- S+A
                 Escreva("Novo Salário: R$",R)
                fimse
           fimse
      fimse

Fimalgoritmo