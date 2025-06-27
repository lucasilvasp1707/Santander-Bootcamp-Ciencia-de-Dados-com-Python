teste = input("informe o texto")
REF= ["A","E","I","O","U"]

for i in teste:
    if i.upper() in REF:
        print(i, end=" " )

for numero in range(4,11,2):
    print(numero, end=" ")


opcao =1 
while opcao != 0:
    print("")
    opcao = int(input("[1]-sacar \n [2]- extrato \n 0-sair digite opção desejada"))
    
    if opcao == 1:
        print("sacou")

    elif opcao == 2:
        print("mostrar extrato")

print("obrigado")            