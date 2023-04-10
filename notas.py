nome = input("digite seu nome: ")
print('o nome digitado foi:',nome)

numero_01 = float(input("digite aqui a sua primeira nota: "))
numero_02 = float(input("digite aqui sua segunda nota: ")) 

media = (numero_01 + numero_02) / 2

print("resultado da soma e: ",media)

if media >= 7:
    print("aprovado")
elif media < 7 and media >= 6:
    print("recuperacao")
else:
    print("reprovado")












