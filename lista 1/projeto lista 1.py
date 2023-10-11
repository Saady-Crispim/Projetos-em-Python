print("menu: ")
print("1- Imprimindo os valores das variáveis")
print("2- Realizando operações e imprimindo resultados com 2 numeros inteiros")
print("3- Convertendo Celsius para Fahrenheit")
print("4- Convertendo Milhas para quilômetros")
print("5- Função para calcular o valor de delta")
print("6- Lendo preços do etanol e gasolina")
print("7- Lendo dimensões do salão e da cerâmica")
a = int(input("Digite a opção desejada: "))

if (a < 1 or a > 7):
    print("\nvalor invalido")
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")

if (a == 1):
    v1 = int(input("\ndigite quantas coisas serão guardadas: "))
    info = []
    while 1 <= v1:
        v2 = input("digite o que será guardado (ex: nome, endereço cep...), com a respectiva resposta: ")
        info.append(v2)
        v1 -= 1
    v3 = input("gostaria de saber o que esta na sua lista? ")
    if v3 == "sim":
        print("todas as suas informações são: ")
        print(info)
    elif v3 == "não":
        print("código encerrado")
    
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")

if (a == 2):
    print("\ndado dois coeficientes inteiros, será imprimido suas respostas sobre as 4 operações aritméticas simples")
    v1 = int(input("digite o coeficiente a: "))
    v2 = int(input("digite o coeficiente b: "))
    soma = v1 + v2
    print(v1,"+",v2, "=", soma)
    sub = v1 - v2
    print(v1,"-",v2, "=", sub)
    div = v1 / v2
    print(v1,"/",v2, "=", div)
    multi = v1 * v2
    print(v1,"*",v2, "=", multi)
        
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")
    
if( a == 3):
    perg = input("\nvocê gostaria de saber a conversão para celsius ou para fahrenheit?\nfahrenheit = F\ncelsius = C\n para o que quer converter? ")
    if (perg == "F"):
        v1 = float(input("\npara saber a conversão de graus celsius para fahrenheit\ndigite o grau Celsius: "))
        v2 = (v1*9)/5+32
        print("\no valor em celsius: ", v1, "\nem fahrenheit é: ", v2)
    elif (perg == "C"):
        v1 = float(input("\npara saber a conversão de graus fahrenheit para celsius\ndigite o grau fahrenheit: "))
        v2 = (v1-32)/1.8
        print("\no valor em fahrenheit: ", v1, "\nem celsius é: ", v2)
    else:
        print("\ninformação invalida\nlembre-se que celsius ou fahrenheit estejam representadas corretamente(em letras F ou C)")
    
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")

if (a == 4):
    v1 = input("\nGostaria de saber a conversão de milhas para quilometros ou quilometros para milhas?\n para milhas: MI\n para quilometros: KM\n")
    if (v1 == "MI"):
        v2 = float(input("digite a distancia em KM: "))
        mi = v2/1.60934
        print("a distancia em km:", v2, "em milhas é: ", mi)
    elif (v1 == "km"):
        v2 = float(input("digite a distancia em Milhas: "))
        mi = v2*1.60934
        print("a distancia em milhas", v2, "em quilometros é: ", mi)
    else:
        print("opção inválida\n certifique-se que as representações(KM e MI) estejam corretas.")
    
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")

if (a == 5):
    print("\npara saber o valor de delta é necessario que nos forneça 3 coeficientes...")
    v1 = float(input("coeficiente a:"))
    v2 = float(input("coeficiente b:"))
    v3 = float(input("coeficiente c:"))
    delta = v2**2 -4*v1*v3
    print("\ndelta =b² - 4*a*c\nLogo...\n",v2,"^2 - 4 *",v1,"*",v2,"=",delta)
    
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")

if (a == 6):
    print("\npara saber quanto seria gasto para encher um tanque com relação a cada combustivel(Etanol e gasolina)\nnos forneça os seguintes dados... ")
    v1 = float(input("capacidade do tanque: "))
    v2 = float(input("preço do etanol: "))
    v3 = float(input("preço da gasolina: "))
    v4 = v2/v3
    v5 = v2*v1
    v6 = v3*v1
    if (v4 <= 0.7):
        print("\npara encher um tanque de", v1,"litros\n considerando o preço e a potencia da combustivel o que mais compensa o investimento é no etanol\n veja um comparativo")
        print("etanol * tanque =", v5)
        print("gasolina * tanque =",v6)
        print("etanol / gasolina =",v4)
        print("\ntenha em mente que para o etanol ser mais vantajoso tem que estar abaixo de 0.7(70%) comparado ao preço gasolina comum\nsignifica que para obter a mesma quantidade de energia, é necessário usar mais etanol do que gasolina.\n\n ")
    else:
        print("\npara encher um tanque de", v1,"litros\n considerando o preço e a potencia da combustivel o que mais compensa o investimento é na gasolina\n veja um comparativo")
        print("etanol * tanque =", v5)
        print("gasolina * tanque =",v6)
        print("etanol / gasolina =",v4)
        print("\ntenha em mente que para o etanol ser mais vantajoso tem que estar abaixo de 0.7(70%) comparado ao preço gasolina comum\nsignifica que para obter a mesma quantidade de energia, é necessário usar mais etanol do que gasolina.\n\n ")
    
    v7 = input("para o programa encerrar pressione qualquer tecla")
    if (v7 == "enter"):
        print("acabou o código")

if (a == 7):
    print("\npara revestir um salão retangular com um piso cerâmico, cujas peças têm o mesmo tamanho\n nos forneça os seguintes dados:")
    v1 = float(input("comprimento do salão retangular(valores reais expressos em metros): "))
    v2 = float(input("largura do salão retangular(valores reais expressos em metros): "))
    v3 = int(input("largura da cerâmica a ser empregada(valores inteiros em milimetros): "))
    v4 = int(input("comprimento da cerâmica a ser empregada(valores inteiros em milimetros): "))

    v5 = v1*1000/v4
    v6 = v2*1000/v3
    v7 = v5*v6
    v8 = int(v7)
    print("\na quantidade de peças de piso que deverão ser compradas são:", v8)
    v9 = input("\n\npara encerrar o programa pressione qualquer tecla")
    
    if v9 == "enter":
        print("a")