#Escreva um programa Python que leia números reais fornecidos pelo usuário até que sua soma seja 100 ou mais...
num = float(input("digite um numero que deseja que seja somado consecutivamente até dar + ou - 100: "))
valor = 0
contador = 0
media = 0
print("soma")
while num <= 100:
    soma = num + num
    print(f"{num} + {num} = {soma}")
    num += num
    contador += 1
#...Então o programa deve apresentar a quantidade de números fornecidos...
print(f"Foram fornecidos {contador} numeros")

#...e sua média aritmética simples.
media = soma/contador
print("sua média é ", media)