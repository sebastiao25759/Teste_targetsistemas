nome = input("Digite um nome: ")
invNome = ""

for i in range(len(nome), 0, -1):

    invNome += nome[i-1]

print(invNome)