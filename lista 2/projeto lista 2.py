while True:
    print("\n-------------------------------------------------------------------------------------------------------\n")
    print("\Menu:")
    print("1. tabuada de um número inteiro;")
    print("2. apresentar a quantidade de números fornecidos e sua média aritmética simples;")
    print("3. indicando se ele é par ou não;")
    print("4. indicando se ele é primo ou não;")
    print("5. quantidade de números positivos fornecidos, a quantidade de números negativos fornecidos;")
    print("6. tabela com os resultados de x = a*x + b para os valores de x de -5.0 a +5.0;")
    print("7. Calcule o (delta = b² - 4*a*c) e as raízes desta equação;")
    print("8. leia um número inteiro (naturalmente na base 10) convertendo-o para seu equivalente em binário (base 2);")
    print("9. Sair")
    v1= int(input("Selecione uma das opções: "))
    if(v1 == 1):
        print("\n você escolheu, 1. tabuada de um número inteiro ")
        a = int(input("escreva um numero inteiro para receber sua tabuada: "))
        b = 1
        print("inicio")
        while (b < 11):
            c = a*b
            print(a, "x", b, "=", c)
            b += 1
        print("final")
    elif (v1 == 2):
        print("\n você escolheu, 2. apresentar a quantidade de números fornecidos e sua média aritmética simples")
        quantidade = 0
        soma = 0
        while (soma < 100):
            a = float(input("digite um numero até que sua soma seja 100 ou mais: "))
            soma = soma + a
            quantidade = quantidade + 1
            print("soma", soma ,"repetição", quantidade)
            media = soma/quantidade
        print("\n a media aritmética simples é", media)
    elif (v1 == 3):
        print("\n você escolheu, 3. indicando se ele é par ou não")
        num = int(input("digite um numero e saiba se ele é par ou impar: "))
        if (num % 2 == 0):
            print("seu numero é par")
        else:
            print("seu numero é impar")
    elif (v1 == 4): 
        print("\n você escolheu, indicando se ele é primo ou não")
        num = int(input("Digite um numero inteiro: "))
        valor = 2
        primo = 1
        # Verifica se o número é menor que 1
        if num < 1:
            print("zn Valor inválido, por favor digite um numero inteiro de 1 para cima")
            exit()
        # Entra em um loop enquanto valor for menor que a metade do número mais 1
        #nenhum numero maior que a metade pode ser divisor
        while valor < num//2 + 1:
            # Verifica se o número é divisível por valor
            if num % valor == 0:
            # Se for, muda o valor de primo para False e sai do loop
                primo = 0
                break
            valor += 1
        if primo == 1:
            # Se for True, mostra uma mensagem dizendo que o número é primo
            print("Seu numero é primo")
        else:
        # Se for False, mostra uma mensagem dizendo que o número não é primo
            print("Seu numero não é primo")
    elif(v1 == 5):
        print("\n você escolheu, 5. quantidade de números positivos fornecidos, a quantidade de números negativos fornecidos")
        va_de_ctrl = 1
        quantidade = 0
        while va_de_ctrl != 0:
            num = float(input("\ndigite a quantidade de numeros que quiser, quando digitar 0 sera expostoa quantidade de numeros: "))
            quantidade += 1
            if num == 0:
                print("código encerrado, a quantidade de numeros é: ", quantidade)
                exit()
    elif(v1 == 6):
        print("\n você escolheu, 6. tabela com os resultados de x = a*x + b para os valores de x de -5.0 a +5.0;")
        a = float(input("digite o coeficiente 'a': "))
        b = float(input("digite o coeficiente 'b': "))
        x1= -5
        x2= 5
        x_1 = a*x1 + b
        x_2 = a*x2 + b
        print("X")
        while x1 <= x2:
            print(x1)
            x1 += 0.5
        print("x = a*x + b")
        while x_1 <= x_2:
            print(x_1)
            x_1 += 1
        print("\n", "x =",x_1,"y =", x_2)
    elif(v1 == 7):
        import math
        print("\n você escolheu, 7. Calcule o (delta = b² - 4*a*c) e as raízes desta equação;")
        a = float(input("digite o coeficiente 'a': "))
        b = float(input("digite o coeficiente 'b': "))
        c = float(input("digite o coeficiente 'c': "))
        delta= b**2 - 4*a*c
        print("delta =", b,"**2 - 4*",a, "*", c)
        print("delta = ", delta)
        if delta >= 1: 
            x1 = (-b + math.sqrt(delta))/(2*a)
            print("x1 = ",x1)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("x2 = ",x2)
        elif delta == 0:
            x = -b / (2*a) # parênteses
            print("x = ",x)
        else:
            print("A equação não possui raízes reais")
    elif(v1 == 8):
        print("\n você escolheu, 8. leia um número inteiro (naturalmente na base 10) convertendo-o para seu equivalente em binário (base 2);")
    elif (v1 == 9):
        break
    else:
        print("Opção inválida")