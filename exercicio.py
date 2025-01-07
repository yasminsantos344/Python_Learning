"""
Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais
qual será o valor do mesmo com desconto de (??)%.
04 - área de um círculo (pi = 3,141592)
06 - conversão de reais para dolar
07 - conversão de dolar para reais

"""

# 01 #

largura_ret = float(input("Qual a largura do retângulo? "))
comprimento_ret = float(input("Qual o comprimento do retângulo? "))

area_ret = largura_ret * comprimento_ret
print("A área do retângulo e: ", area_ret)

# 02 #

largura_quad = float(input("Qual a largura do quadrado? "))
comprimento_quad = float(input("Qual o comprimento do quadrado? "))

area_quad = largura_quad * comprimento_quad
print("A área do quadrado e: ", area_quad)

# 03 #

valor = float(input("Qual o valor do produto? "))
desconto = float(input("Informe o desconto em porcentagem: "))

total = valor - ((desconto / 100) * valor)
print("O valor do produto será: ", total)

# 04 #

pi = 3.141592
raio = float(input("Qual o raio do circulo? "))

area_circulo = pi * (raio ** 2)
print("A area do circulo e: ", area_circulo)

# 05 #

reais = float(input("Digite a quantia de reais "))

turn_dolar = reais * 6.11
print(reais, " equivalem a ", turn_dolar, " em dolar")

# 06 #

dolar = float(input("Digite a quantia de dolares "))

turn_real = dolar / 6.11
print(dolar, " equivalem a ", turn_real, " em reais")
