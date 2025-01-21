"""
Maiúsculas e minúsculas
Símbolos e espaços

Criptografia de substituição

Security = chave
5ecur!ty = senha

hex

1 = 1
2 = 2
até 9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
14 = F
"""

chave = input("Digite a base da sua senha: ")
SENHA = ""

for letra in chave:
    if letra in "Aa":
        SENHA = SENHA + "1"
    elif letra in "Bb":
        SENHA = SENHA + "@"
    elif letra in "Cc":
        SENHA = SENHA + "12"
    elif letra in "Dd":
        SENHA = SENHA + "17"
    elif letra in "Ee":
        SENHA = SENHA + "14"
    elif letra in "Ff":
        SENHA = SENHA + "*"
    elif letra in "Rr":
        SENHA = SENHA + "#"
    elif letra in "Ss":
        SENHA = SENHA + "%"
    elif letra in "Mm":
        SENHA = SENHA + "$"
    else:
        SENHA = SENHA + letra

print(SENHA)
