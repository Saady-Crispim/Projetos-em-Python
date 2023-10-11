#importar biblioteca
import random

#[  ] Formatação
sequencia = "-_-"
repeticoes = 20
resultado = sequencia * repeticoes

#[  ] Número pré definidos de bolas na caixa
bolas=int(input("escreva a quantidade de bolas que haverá dentro da caixa: "))

#[  ] Random para saber quem começa eu ou o computador 
inicio= random.randint(1,2)
print("1 = usuario")
print("2 = computador")
print("quem inicia = ", inicio)
print(resultado)

#[  ] While é interrompido quando as bolas na caixa dor < ou = 0
while (bolas>0):

    #[  ] Se i==1 usuário, elif i==2 computador
    if inicio==1:
        valores_permitidos = [1, 2, 3, 4]
        while True:
            usuario = int(input("Digite um valor[1, 2, 3, 4]: "))
            if usuario in valores_permitidos:
                break
        print(usuario, "usuário")

        #[  ] Random num de bolas comp de 1 a 4 
        computador = random.randint(1,4)
        print(computador, "computador")
    elif inicio==2:
  
        #[  ] Random num de bolas comp de 1 a 4 
        computador = random.randint(1,4)
        print(computador, "computador")
  
        #[  ] Lista designa os valores permitidos
        valores_permitidos = [1, 2, 3, 4]


        while True:
            usuario = int(input("Digite um valor[1, 2, 3, 4]: "))
            #[  ] se o valor estiver dentro da lista o cód encerra
            if usuario in valores_permitidos:
                break
            print(usuario, "usuário")
    #[  ] números de bolas menos qtde selecionada
    bolas = bolas-computador-usuario
    print("\n faltam", bolas," bolas\n")
print(resultado)
#[  ] saber quem ganhou
if usuario <= inicio:
    print("O usuário perdeu!")
else:
    print("O computador perdeu!")