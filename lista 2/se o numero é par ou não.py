# receba um número inteiro
num = int(input("digite um numero inteiro e saiva se par ou não: "))
#se ele é par ou não.
if num % 2 == 0:
   print("seu numero é par")
else:
 print("seu numero é ímpar")
"""
explicação: % é o resto de uma divisão, logo se o numero for divisivel 
por 2 tendo o resto 2 ou 0 resulta em par,
ex: 20/2 = 10
desses 10 restou 0
"""