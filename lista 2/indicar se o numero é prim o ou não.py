num = int(input("Digite um numero inteiro: "))
valor = 2
primo = 1
    # Verifica se o número é menor que 1
if num < 1:
    print("Valor inválido, por favor digite um numero inteiro de 1 para cima")
    exit()
    # Entra em um loop enquanto valor for menor que a metade do número mais 1
    #nenhum numero maior que a metade pode ser divisor
while valor < num//2 + 1:
    # Verifica se o número é divisível por valor///o numero ser divido por 2, apenas encurta o processo para não usar tanta memoria sem necessidade
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