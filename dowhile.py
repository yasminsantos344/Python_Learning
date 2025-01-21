"""

do while

Código para advinhar número

"""

palpite = 0
numero = 9

print("Advinhe qual o numero correto")

while palpite != numero:
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero:
        print(f"Você acertou! O número secreto é {numero}")
        break


