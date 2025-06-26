saldo =1000
saque =200
limite =100
conta_especial = True;

saldo > saque

print(saldo > saque and  saque<limite)
print(saldo > saque or saque<limite)
print (not saldo >saque)

print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

#and tudo tem que ser true
#or apenas um tem que ser true