""" Escopo de variáveis """

"""
variaveis globais

variaveis locais

"""

x = 5 #variável global (feita fora de um bloco e podem ser utilizadas por outras funções)
print("valor da variável global:", x)

def funcao():
    x = 3
    print("Valor da variavel local: ", x)

funcao()

""" Comentar ao lado é uma maneira de identificar o que essas variáveis significam """
y = 'Gabriel' #nome
z = 1.74 #altura
t = "000.000.000-00"   #cpf
l = 23  #idade

""" um jeito melhor é dar às variáveis seu propósito """

nome = 'Gabriel'
altura = 1.74
cpf = "000.000.000-00"
idade = 23

