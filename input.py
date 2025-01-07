"""
Função inpu() - Função para receber dados do usuário

"""

# 1° Forma #

nome = input("Qual e o seu nome? ")
print("Olá, ", nome)

nome = input("Qual e o seu idade? ")
print("Sua idade e: ", nome)

# 2° Forma #

nome = input("Qual o seu nome?")
idade = input("Qual a sua idade? ")

print("Seu nome eh: {0} e Sua idade eh: {1}".format(nome, idade))

# 3° Forma #

nome = input("Qual o seu nome?")
idade = input("Qual a sua idade? ")

print(f"Seu nome e: {nome} e Sua idade e: {idade}")