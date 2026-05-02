Algoritmo "exercicio 41"

Var
   A,P,IMC, A2:real


Inicio
      Escreva("Qual sua altura? em Metros: ")
      Leia(A)
      Escreva("Qual seu peso? em KG: ")
      Leia(P)
      A2 <- (A^2)
      IMC <- P/A2
      Escreval("IMC =", IMC)
      se (IMC < 18.4) entao
      Escreva ("Magrelo")
      senao
           se (IMC >= 18.5) e (IMC < 25) entao
           Escreva("Normal")
           senao
                se (IMC >= 25) e (IMC < 30) entao
                Escreva("Gordo")
                senao
                     se(IMC >= 35) entao
                     Escreva ("Gordao")
                     fimse
                fimse
           fimse
      fimse


Fimalgoritmo