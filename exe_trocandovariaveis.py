"""

Exercício Trocando Variáveis

"""

X = input("Insira o valor de x: ")
Y = input("Insira o valor de y: ")

# Criaremos uma variável temporária #

temp = X
X = Y
Y = temp

print(f"O valor de x depois da troca: {X}")
print(f"O valor de Y depois da troca: {Y}")
