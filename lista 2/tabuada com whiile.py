### dado fornecido pelo usuario
num_primo = int(input("Digite o numero primo para resultar em sua tabuada: "))
inicio = 0 ### variavel que dara inicio a contagem
print("tabuada")
while inicio <= 10:
    tabuada = num_primo*inicio
    inicio += 1
    print(f"{num_primo} x {inicio} = {tabuada}")
    #As f-strings permitem que você insira expressões Python dentro das strings,
    #tornando a formatação de strings mais concisa e legível. 
    #Você pode colocar expressões dentro de chaves {}dentro da string e o valor dessas expressões
    #será calculado e inserido na string
    
print("fim")
