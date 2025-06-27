def sacar(valor: int):
    saldo =500
    if saldo >= valor:
        print("sacou")
        saldo -=valor
        print("seu saldo",saldo)


sacar(100)        


def exibanome(nome:str):
    nome2 =nome;
    print(nome2)

exibanome("lucas")

def tirar_cnh(idade:int):
    if idade >= 18:
        print("pode tirar cnh ja é maior de idade")

    elif idade >=16 and idade <18:
        print('pode tirar com autorização dos pais')    

    else:
        print("não pode tirar a cnh")
    status ="sucesso " if idade >=18 else "nao pode tirar a cnh no momento"    
    print( status ,"resultado do if ternario" )

tirar_cnh(18)         


#if ternario

