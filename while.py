"""

Estrututas de repetição

while
for
do while

"""

A = 0

while A <= 5:
    print(A)
    print(A <= 5)
    if A == 3:
        break
    A = A + 1
else:
    print(f"A não é menor ou igual a 5. Valor de a: {A}")

print("Resultado final de A: ", A)
print(A <= 5)
