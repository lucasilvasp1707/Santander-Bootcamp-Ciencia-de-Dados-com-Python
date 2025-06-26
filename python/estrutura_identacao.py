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
